from datetime import datetime
from configuration import db



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    user_product = db.relationship('Products', backref='users', lazy=True)


    def __repr__(self):
        return 'id:{}, sname:{}, email:{}, pswd:{},'.format(self.id, self.sname, self.email, self.pswd)