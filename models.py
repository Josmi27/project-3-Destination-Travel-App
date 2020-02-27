import flask_sqlalchemy, app, os



app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(250))
        
    def __init__(self, t):
        self.text = t
        
        
    def __repr__(self):
        return '<Message text: %s>' % self.text 
