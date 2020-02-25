import os
import flask, flask_socketio, flask_sqlalchemy
import models

app = flask.Flask(__name__)
socketio= flask_socketio.SocketIO(app)



@app.route('/')
def index():
    addresses = models.Message.query.all()
    html = ['<li>' + a.address + '</li>' for a in addresses]
    return '<ul>' + ''.join(html) + '</ul>'
    

@socketio.on('connect')
def on_connect():
    print("Someone connected!")
    socketio.emit('update',{
        'data': 'Got your connection'
    })


if __name__ == '__main__':
    
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )