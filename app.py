import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2
import chatbot
import functools
from flask_oauth import OAuth
from flask import redirect, request, url_for, g, flash
from flask import render_template
from urllib.parse import urlparse
app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models
from flask import session

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

oauth = OAuth()

# Use Twitter as example remote application
twitter = oauth.remote_app('twitter',
base_url='https://api.twitter.com/1/',
request_token_url='https://api.twitter.com/oauth/request_token',
access_token_url='https://api.twitter.com/oauth/access_token',
authorize_url='https://api.twitter.com/oauth/authenticate',
# the consumer keys from the twitter application registry.
consumer_key='qukgAQr6KLxBk6wwvImUMvAsx',
consumer_secret='58BO5DB0gmL1edgdRXnxXpEgrOMoo1KzMt4oOx7NCiUxONDEka'
)

@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

#Twitter API Search for Tweets
# twitter_search = "https://api.twitter.com/1.1/search/tweets.json?q=yummy%20donuts&src=typed_query"

# #Twitter Retrieval from Search
# twitter_response = random.randint(0,9)


# #Authorization
# oauth = requests_oauthlib.OAuth1(
## API Key
# "qukgAQr6KLxBk6wwvImUMvAsx", 
## API Secret
# "58BO5DB0gmL1edgdRXnxXpEgrOMoo1KzMt4oOx7NCiUxONDEka",
##Access Token
# "1223192085756596225-UIVDa9WQSMyp3IqJgz7poKxvppykg2",
## Access Token Secret
# "DjzlFxxcCxJ4sP2QSXem9KANGFHKi1RgIIBSa9JPPKlof"
# )

# response = requests.get(twitter_search, auth=oauth)
# json_body = response.json()




@app.route('/')
def hello():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
    return flask.render_template('index.html')

@app.route('/login')
def login():
    return twitter.authorize(callback=url_for('oauth_authorized', None))

@app.route('/logout')
def logout():
    session.pop('screen_name', None)
    flash('You were signed out')
    return redirect(url_for('index'))

@app.route('/oauth-authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    access_token = resp['oauth_token']
    session['access_token'] = access_token
    session['screen_name'] = resp['screen_name']
    
    session['twitter_token'] = (
    resp['oauth_token'],
    resp['oauth_token_secret']
    )
    
    return redirect(url_for('index'))

@socketio.on('connect') 
def on_connect():
    messages = models.Message.query.all()
    array = []
    for m in messages:
        array.append(
            [m.text]
        )
    print('Someone connected!')
    
    socketio.emit('message array',{
     'data': array
    }, broadcast=True)
    


    
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })
    
@socketio.on('new message')
def handleMessage(data):
    username = data['Username']
    current_message = data['Message']
    
    def is_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
            
            
    if current_message[:2] == '!!':
        username = "Destination Travel Bot"
        called_class = chatbot.Chatbot()
        final_response = called_class.response(current_message)
        new_message = models.Message("{}: \n {}".format(username, final_response))
        models.db.session.add(new_message) 
        models.db.session.commit()
    #joy working with database table
    elif current_message[:2] == '!! PR-Music':
        username = "Destination Travel Bot"
        class_call = chatbot.Chatbot()
        final_response = class_call.response(current_message)
        new_message = models.Genius("{}: \n {}".format(username, final_response))
        models.db.session.add(new_message) 
        models.db.session.commit()
   
    elif is_url(current_message) is True:
        hyperlink_format = '<a href="{link}">{text}</a>' #doesn't work now
        hyperlink_format.format(link=current_message, text ='foo bar')
        link_text = hyperlink_format.format
        message_now = models.Message(link_text)
        models.db.session.add(message_now)
        models.db.session.commit()
        
    else:
        info = models.Message("{}: \n {}".format(username, data['Message']))
        models.db.session.add(info)
        models.db.session.commit()
        
    
    return on_connect()

if __name__ == '__main__':   
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
