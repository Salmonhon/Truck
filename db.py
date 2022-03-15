from datetime import datetime
from configuration import db, ma



izbranniy = db.Table("izbranniy",
                    db.Column("k_product", db.Integer, db.ForeignKey('klient_products.id')),
                    db.Column("user", db.Integer, db.ForeignKey('driver.id')))

izbranniy_k = db.Table("izbranniy_k",
                    db.Column("d_product", db.Integer, db.ForeignKey('driver_products.id')),
                    db.Column("user", db.Integer, db.ForeignKey('klient.id')))

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    driver_product = db.relationship('Driver_products', backref='driver', lazy=True)
    following = db.relationship('Klient_products', secondary=izbranniy, backref='izbranniy', lazy='select')

    def __init__(self,sname,email,pswd):
        self.sname = sname
        self.email = email
        self.pswd = pswd


class DriverSchema(ma.Schema):
    class Meta:
        fields = ('id','sname', 'email', 'pswd')


driver_schema = DriverSchema()
drivers_schema = DriverSchema(many=True)


class Klient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pswd = db.Column(db.String(100), nullable=False)
    klinet_product = db.relationship('Klient_products', backref='klient', lazy=True)
    following = db.relationship('Driver_products', secondary=izbranniy_k, backref='izbranniy_k', lazy='select')

    def __init__(self, sname, email, pswd):
        self.sname = sname
        self.email = email
        self.pswd = pswd


class KlientSchema(ma.Schema):
    class Meta:
        fields = ('id','sname', 'email', 'pswd')


klient_schema = KlientSchema()
klients_schema = KlientSchema(many=True)



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

    # def __init__(self, img, date, obyom, type_kuzov, lokatsiya_strana, lokatsiya_gorod, phone, driverID):
    #     self.img = img
    #     self.date = date
    #     self.obyom = obyom
    #     self.type_kuzov = type_kuzov
    #     self.lokatsiya_strana = lokatsiya_strana
    #     self.lokatsiya_gorod = lokatsiya_gorod
    #     self.phone = phone
    #     self.driverID = driverID


class DriverProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', "img", "date", "obyom", "type_kuzov", "lokatsiya_strana", "lokatsiya_gorod", "phone", "driverID")


driver_product_schema = DriverProductsSchema()
driver_products_schema = DriverProductsSchema(many=True)


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

    # def __init__(self, title, start_starana, klientID, text, start_gorod, finish_starana, finish_gorod, date, obyom, type_kuzov, phone):
    #     self.title = title
    #     self.date = date
    #     self.obyom = obyom
    #     self.type_kuzov = type_kuzov
    #     self.start_starana = start_starana
    #     self.start_gorod = start_gorod
    #     self.finish_starana = finish_starana
    #     self.finish_gorod = finish_gorod
    #     self.text = text
    #     self.phone = phone
    #     self.klientID = klientID


class ClientProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'type_kuzov', 'start_strana', 'start_gorod', 'finish_strana', 'finish_gorod', 'obyom', 'text', 'date', 'phone', 'klientID')


klient_product_schema = ClientProductsSchema()
klient_products_schema = ClientProductsSchema(many=True)