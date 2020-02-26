import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2
import chatbot


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
    }, broaadcast=True)
    


    
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })
    
@socketio.on('new message')
def handleMessage(data):
    u_message = data['Message']
    u2_message = models.Message(data['Message'])
    
    current_message = data['Message']

    if current_message[:2] == '!!':
        called_class = chatbot.Chatbot()
        final_response = called_class.response(current_message)
        new_message = models.Message(final_response)
        models.db.session.add(new_message)
        models.db.session.commit()
   
    else:
        info = models.Message(data['Message'])
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
