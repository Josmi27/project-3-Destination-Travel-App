import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2
import chatbot

import functools

from urllib.parse import urlparse
app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models

@app.route('/')
def hello():
 
    return flask.render_template('index.html')

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
