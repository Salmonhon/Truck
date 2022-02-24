
from configuration import app, db
from flask_bcrypt import Bcrypt
from flask import session, request, json, jsonify, redirect
from db import Driver, Klient, Driver_products,Klient_products
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
sec = URLSafeTimedSerializer('SECRETKEYITSISSECRETNAXUYILYA')
bcrypt = Bcrypt(app)


@app.before_first_request
def creat_all():
    db.create_all()

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
        if Driver.query.filter_by(email=email).first():
            return 'Email registred'
        else:
            account = Driver(sname=name, email=email, pswd=hash_pswd)
            db.session.add(account)
            db.session.commit()
            return 'succesuful registred'
    else:
        if Klient.query.filter_by(email=email).first():
            return 'Email registred'
        else:
            account = Klient( sname=name, email=email, pswd=hash_pswd)
            db.session.add(account)
            db.session.commit()
            return 'succesuful registred'


@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    email = request_data['email']
    pswd = request_data['password']
    flag = request_data['flag']
    if flag == '1':
        author_login = Driver.query.filter_by(email=email).first()
        print(author_login.pswd)
        print(bcrypt.check_password_hash(author_login.pswd, pswd))
        if author_login and bcrypt.check_password_hash(author_login.pswd, pswd):
            session['id'] = author_login.id
            return {
                'id': author_login.id,
                'type': 'Driver'
            }
        else:
            return 'Password or email is not correct'
    else:
        author_login = Klient.query.filter_by(email=email).first()
        if author_login and bcrypt.check_password_hash(author_login.pswd, pswd):
            session['id'] = author_login.id
            return {
                'id': author_login.id,
                'type': 'Driver'
            }
        else:
            return 'Password or email is not correct'

@app.route('/logout')
def logout():
    session.clear()  # remove author from session
    return redirect('/')

def driver_product_serializer(Driver_products):
    return {
        'id': Driver_products.id,
        'img': Driver_products.img,
        'date': Driver_products.date,
        'obyom': Driver_products.obyom,
        'type_kuzov': Driver_products.type_kuzov,
        'lokatsiya_strana': Driver_products.lokatsiya_strana,
        'lokatsiy_gorod': Driver_products.lokatsiya_gorod,
        'phone': Driver_products.phone,
        'driverID': Driver_products.driverID
    }


def klient_product_serializer(Klient_products):
    return {
        'id': Klient_products.id,
        'title': Klient_products.title,
        'type_kuzov': Klient_products.type_kuzov,
        'start_lokatsiya_A': Klient_products.start_lokatsiya_A,
        'finish_lokatsiya_B': Klient_products.finish_lokatsiya_B,
        'obyom': Klient_products.obyom,
        'text': Klient_products.text,
        'date': Klient_products.date,
        'phone': Klient_products.phone,
        'klientID': Klient_products.klientID
    }

def Driver_serializer(Driver):
    return {
        'id': Driver.id,
        'sname': Driver.sname,
        'email': Driver.email,
        'password': Driver.pswd,

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

@app.route('/products', methods=['GET'])
def products():
    return jsonify([*map(driver_product_serializer, Driver_products.query.all())])
# def products_2():
#     return jsonify([*map(klient_product_serializer, Klient_Products.query.all())])


@app.route('/add_product', methods=['POST'])
def add_product():
    request_data = request.get_json()
    flag = request_data['flag']
    id_sesiya = request_data['id']
    if flag == '1':
        author_login = Driver.query.filter_by(id=id_sesiya).first()
        print(author_login)

        img = request_data['img']
        obyom = request_data['obyom']
        type_kuzov = request_data['type_kuzov']
        lokatsiya_strana = request_data['lokatsiya_strana']
        lokatsiya_gorod = request_data['lokatsiya_gorod']
        phone = request_data['phone']
        print(img, obyom, type_kuzov, lokatsiya_strana, lokatsiya_gorod, phone, token)
        product = Driver_products(img=img, obyom=obyom, type_kuzov=type_kuzov, lokatsiya_strana=lokatsiya_strana, lokatsiya_gorod=lokatsiya_gorod, phone=phone, driverID=author_login)
        print(product)
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

        product = Klient_products(title=title, type_kuzov=type_kuzov, start_staran=start_staran, start_gorod=start_gorod, finish_strana=finish_strana, finish_gorod=finish_gorod, obyom=obyom, text=text)
        db.session.add(product)
        db.session.commit()
        return 'Succseful added'



if __name__=="__main__":
    app.run(debug=True)