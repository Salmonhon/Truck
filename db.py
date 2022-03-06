from datetime import datetime
from configuration import db




class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    driver_product = db.relationship('Driver_products', backref='driver', lazy=True)


    def __repr__(self):
        return 'id:{}, sname:{}, email:{}, pswd:{}'.format(self.id, self.sname, self.email, self.pswd)


class Klient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    klinet_product = db.relationship('Klient_products', backref='klient', lazy=True)



    def __repr__(self):
        return 'id:{}, sname:{}, email:{}, pswd:{}'.format(self.id, self.sname, self.email, self.pswd)



class Driver_products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(), nullable=True)
    date = db.Column(db.DateTime, default=datetime.today)
    obyom = db.Column(db.String(), nullable=False)
    type_kuzov = db.Column(db.String(), nullable=False)
    lokatsiya_strana = db.Column(db.String(), nullable=False)
    lokatsiya_gorod = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    driverID = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)

    def __repr__(self):
        return 'id:{}, img:{}, date:{}, obyom:{}, type_kuzov:{}, lokatsiya_strana:{}, lokatsiya_gorod:{}, phone:{}, driverID:{}'.format(self.id, self.img, self.date, self.obyom, self.type_kuzov, self.lokatsiya_strana, self.lokatsiya_gorod, self.phone, self.driverID)

class Klient_products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type_kuzov = db.Column(db.String, nullable=False)
    start_starana = db.Column(db.String, nullable=False)
    start_gorod = db.Column(db.String, nullable=False)
    finish_starana = db.Column(db.String, nullable=False)
    finish_gorod = db.Column(db.String,nullable=False)
    obyom = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.today)
    phone = db.Column(db.Integer, nullable=False)
    klientID = db.Column(db.Integer, db.ForeignKey('klient.id'), nullable=False)

    def __repr__(self):
         return 'id:{}, title:{}, type_kuzov:{}, start_strana:{}, start_gorod:{}, finish_strana:{}, finish_gorod:{}, obyom:{}, text:{}, date:{}, phone:{}, klientID:{}'.format(self.id, self.title, self.type_kuzov, self.start_starana, self.start_gorod, self.finish_starana, self.finish_gorod, self.obyom, self.text, self.date, self.phone,  self.klientID)