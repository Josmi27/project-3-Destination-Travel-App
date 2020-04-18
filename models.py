import flask_sqlalchemy, app, os

 
# os.environ['DATABASE_URL'] = 'postgresql://joyelias:welcome@localhost/postgres'
# app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:password@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    # user = db.Column(db.String(250))
    text = db.Column(db.String(250))
        
    def __init__(self,t):
        # self.name = u
        self.text = t
        
        
    def __repr__(self):
        return "{'Message text: %s'}" % (self.text) 


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    # user = db.Column(db.String(250))
    currency = db.Column(db.String(250))
        
    def __init__(self,c):
        # self.name = u
        self.currency = c
        
        
    def __repr__(self):
        return "{'Currency: %s'}" % (self.currency) 