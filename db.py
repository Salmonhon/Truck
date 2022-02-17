from datetime import datetime
from configuration import db



class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    driver_product = db.relationship('Dirver_Products', backref='Driver', lazy=True)


    def __repr__(self):
        return 'id:{}, sname:{}, email:{}, pswd:{},'.format(self.id, self.sname, self.email, self.pswd)


class Klient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    klinet_product = db.relationship('Klient_Products', backref='Klient', lazy=True)


    def __repr__(self):
        return 'id:{}, sname:{}, email:{}, pswd:{},'.format(self.id, self.sname, self.email, self.pswd)



class Dirver_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.File, nullable=True)
    data = db.Column(db.Data)  #buyodayam data type qilishin kere
    obyom = db.Column(db.Integer, nullable=False)
    type_kuzov = db.Column(db.String, nullable=False)
    startA = db.Column(db.String, nullable=False)
    startB = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.Data, nullable=False) #salmonhon mashini togillab qoy
    driverID = db.relationship # mashiniyam togilab ulab qoy


class Klient_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type_kuzov = db.Column(db.String, nullable=False)
    startA = db.Column(db.String, nullable=False)
    startB = db.Column(db.String, nullable=False)
    obyom = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String, nullable=False)
    data = db.Column(db.Data)#togillab qoy buniyam
    deadline = db.Column(db.Data,nullable=False)#togilla attention
    klientId = db.relationship # togillab qoy buniyam
