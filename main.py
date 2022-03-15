from datetime import datetime
from configuration import app
from flask_bcrypt import Bcrypt
from flask import session, request, jsonify, redirect
from db import *
from itsdangerous import URLSafeTimedSerializer
sec = URLSafeTimedSerializer('SECRETKEYITSISSECRETNAXUYILYA')
bcrypt = Bcrypt(app)


@app.before_first_request
def creat_all():
    db.create_all()

@app.route('/')
def first():
    return 'hello'

@app.route('/v1/regist', methods=["POST"])
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


@app.route('/v1/login', methods=['POST'])
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
                'type': 'Klient'
            }
        else:
            return 'Password or email is not correct'

@app.route('/v1/logout')
def logout():
    session.clear()  # remove author from session
    return redirect('/')


@app.route('/v1/products', methods=['GET'])
def products():
    driver_products = Driver_products.query.all()
    d_products = driver_products_schema.dump(driver_products)


    klent_products = Klient_products.query.all()
    k_products = klient_products_schema.dump(klent_products)

    return jsonify({"Driver": d_products,
                    "Klient": k_products})




@app.route('/v1/add_product', methods=['POST'])
def add_product():
    request_data = request.get_json()
    flag = request_data['flag']
    id_sesiya = request_data['id']
    if flag == '1':
        if Driver.query.filter_by(id=id_sesiya).first():
            author_login = Driver.query.filter_by(id=id_sesiya).first()
            img = request_data['img']
            obyom = request_data['obyom']
            type_kuzov = request_data['type_kuzov']
            lokatsiya_strana = request_data['lokatsiya_strana']
            lokatsiya_gorod = request_data['lokatsiya_gorod']
            phone = request_data['phone']
            driverID = request_data['id']
            product = Driver_products(img=img, obyom=obyom, type_kuzov=type_kuzov, lokatsiya_strana=lokatsiya_strana, lokatsiya_gorod=lokatsiya_gorod, phone=phone, driverID=driverID)
            db.session.add(product)
            db.session.commit()
            return 'Succseful added'
        else:
            return "No such kind of Driver"


    else:
        if Klient.query.filter_by(id=id_sesiya).first():
            author_login = request_data['id']
            title = request_data['title']
            type_kuzov = request_data['type_kuzov']
            start_starana = request_data['start_strana']
            start_gorod = request_data['start_gorod']
            finish_starana = request_data['finish_strana']
            finish_gorod = request_data['finish_gorod']
            obyom = request_data['obyom']
            text = request_data['text']
            phone = request_data['phone']

            product = Klient_products(title=title, type_kuzov=type_kuzov, start_starana=start_starana, start_gorod=start_gorod, finish_starana=finish_starana, finish_gorod=finish_gorod, obyom=obyom, text=text, phone=phone, klientID=author_login)
            db.session.add(product)
            db.session.commit()
            return 'Succseful added'
        else:
            return 'No such kind of klient'


@app.route('/v1/profile', methods=['GET', 'POST'])
def profile():
    request_id = request.get_json()
    session_id = request_id['id']
    type = request_id['type']
    if type == 'Driver':
        driver = Driver.query.get(session_id)
        driver_products = Driver_products.query.filter_by(driverID=session_id).all()
        driver_result = driver_schema.dump(driver)
        products = driver_products_schema.dump(driver_products)
        return jsonify({'DRIVER': driver_result,
                        'PRODUCTS': products})
    else:
        klient = Klient.query.get(session_id)
        klent_products = Klient_products.query.filter_by(klientID=session_id).all()
        klient_result = klient_schema.dump(klient)
        products = klient_products_schema.dump(klent_products)
        return jsonify({'KLIENT': klient_result,
                        'PRODUCTS': products})



@app.route('/v1/profile/product/edit/<id>', methods=['POST'])
def edit(id):
    request_data = request.get_json()
    product_id = id
    type = request_data['flag']

    if type == "1":
        img = request_data['img']
        obyom = request_data['obyom']
        type_kuzov = request_data['type_kuzov']
        lokatsiya_strana = request_data['lokatsiya_strana']
        lokatsiya_gorod = request_data['lokatsiya_gorod']
        phone = request_data['phone']


        product = Driver_products.query.get(product_id)
        product.img = img
        product.obyom = obyom
        product.type_kuzov = type_kuzov
        product.lokatsiya_strana = lokatsiya_strana
        product.lokatsiya_gorod = lokatsiya_gorod
        product.phone = phone

        db.session.commit()
        return "Succes edited"
    else:
        title = request_data['title']
        type_kuzov = request_data['type_kuzov']
        start_starana = request_data['start_strana']
        start_gorod = request_data['start_gorod']
        finish_starana = request_data['finish_strana']
        finish_gorod = request_data['finish_gorod']
        obyom = request_data['obyom']
        text = request_data['text']
        phone = request_data['phone']

        k_product = Klient_products.query.get(product_id)
        k_product.title = title
        k_product.type_kuzov = type_kuzov
        k_product.start_starana = start_starana
        k_product.start_gorod = start_gorod
        k_product.finish_starana = finish_starana
        k_product.finish_gorod = finish_gorod
        k_product.obyom = obyom
        k_product.text = text
        k_product.phone = phone

        db.session.commit()
        return "Succes edited"



@app.route('/v1/profile/product/delete/<id>', methods=['DELETE'])
def delete(id):
    request_data = request.get_json()
    product_id = id
    type = request_data['flag']

    if type == '1':
        product = Driver_products.query.get(product_id)
        db.session.delete(product)
        db.session.commit()
        return "Deleted"

    else:
        product = Klient_products.query.get(product_id)
        db.session.delete(product)
        db.session.commit()
        return "Deleted"



if __name__=="__main__":
    app.run(debug=True)



