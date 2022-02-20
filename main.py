

from configuration import app, db
from flask_bcrypt import Bcrypt
from flask import session, request, json, jsonify
from db import Driver, Klient, Driver_products,Klient_Products
bcrypt = Bcrypt(app)


# @app.before_first_request
# def creat_all():
#     db.create_all()

@app.route('/')
def first():
    return 'hello'

@app.route('/regist', methods=["POST"])
def regist():
    request_data = request.get_json()
    name = request_data['name']
    email = request_data['email']
    pswd = request_data['password']
    flag = request_data['flag']
    hash_pswd = bcrypt.generate_password_hash(pswd).decode('utf-8')
    if flag == "1":
        if not Driver.query.filter_by(email=email).first():
            account = Driver(sname=name, email=email, pswd=hash_pswd)
            db.session.add(account)
            db.session.commit()
            return 'succesuful registred'
        else:
            return "Email registred"
    else:
        if not Klient.query.filter_by(email=email).first():
            account = Klient(sname=name, email=email, pswd=hash_pswd)
            db.session.add(account)
            db.session.commit()
            return 'succesuful registred'
        else:
            return 'Email registred'


@app.route('/login')
def login():
    request_data = request.get_json()
    email = request_data['email']
    pswd = request_data['password']
    flag = request_data['flag']
    if flag == '1':
        author_login = Driver.query.filter_by(email=email).first()
        if author_login and bcrypt.check_password_hash(author_login.pswd, pswd):
            session['id'] = author_login.id
            return 'Succseful login', session['id'], 'Driver'
        else:
            return 'Password or email is not correct'
    else:
        author_login = Klient.query.filter_by(email=email).first()
        if author_login and bcrypt.check_password_hash(author_login.pswd, pswd):
            session['id'] = author_login.id
            return 'Succseful login', session['id'], 'Klient'
        else:
            return 'Password or email is not correct'

def driver_product_serializer(Driver_products):
    return {
        'id': Driver_products.id,
        'img': Driver_products.img,
        'date': Driver_products.date,
        'obyom': Driver_products.obyom,
        'type_kuzov': Driver_products.type_kuzov,
        'lokatsiya': Driver_products.lokatsiya,
        'phone': Driver_products.phone,
        'deadline': Driver_products.deadline,
        'driverID': Driver_products.driverID
    }


def klient_product_serializer(Klient_Products):
    return {
        'id': Klient_Products.id,
        'title': Klient_Products.title,
        'type_kuzov': Klient_Products.type_kuzov,
        'start_lokatsiya_A': Klient_Products.start_lokatsiya_A,
        'finish_lokatsiya_B': Klient_Products.finish_lokatsiya_B,
        'obyom': Klient_Products.obyom,
        'text': Klient_Products.text,
        'date': Klient_Products.date,
        'phone': Klient_Products.phone,
        'deadline': Klient_Products.deadline,
        'klientID': Klient_Products.klientID
    }

def Driver_serializer(Driver):
    return {
        'id': Driver.id,
        'sname': Driver.sname,
        'email': Driver.email,
        'password': Driver.pswd,
        'izbranniy_id': Driver.liked
    }

def Klient_serializer(Klient):
    return {
        'id': Klient.id,
        'sname': Klient.sname,
        'email': Klient.email,
        'password': Klient.pswd,
        'izbranniy_id': Klient.liked,
        'user_type': 'Klinet'
    }

@app.route('/products')
def products():
    return jsonify([map(driver_product_serializer)])
def products_2():
    return jsonify([map(klient_product_serializer)])


@app.route('/add_product')
def add_product_driver():
    request_data = request.get_json()
    flag = request_data['flag']

    if flag == '1':
        img = request_data['img'],
        obyom = request_data['obyom'],
        type_kuzov = request_data['type_kuzov']
        lokatsiya_strana = request_data['lokatsiya_strana'],
        lokatsiya_gorod = request_data['lokatsiya_gorod']
        phone = request_data['phone']

        product = Driver_products(img=img, obyom=obyom, type_kuzov=type_kuzov, lokatsiya_strana=lokatsiya_strana, lokatsiya_gorod=lokatsiya_gorod, phone=phone)
        db.session.add(product)
        db.session.commit()
        return 'Succseful added'


    else:
        title = request_data['title']
        type_kuzov = request_data['type_kuzov']
        start_staran = request_data['start_strana']
        start_gorod = request_data['start_gorod']
        finish_strana = request_data['finish_strana']
        finish_gorod = request_data['finish_gorod']
        obyom = request_data['obyom']
        text = request_data['text']

        product = Klient_Products(title=title, type_kuzov=type_kuzov, start_staran=start_staran, start_gorod=start_gorod, finish_strana=finish_strana, finish_gorod=finish_gorod, obyom=obyom, text=text)
        db.session.add(product)
        db.session.commit()
        return 'Succseful added'



if __name__=="__main__":
    app.run(debug=True)