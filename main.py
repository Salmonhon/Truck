

from configuration import app, db
from flask_bcrypt import Bcrypt
from flask import session, request, json
from db import Driver, Klient
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
            return 'Succseful login'
        else:
            return 'Password or email is not correct'
    else:
        author_login = Klient.query.filter_by(email=email).first()
        if author_login and bcrypt.check_password_hash(author_login.pswd, pswd):
            session['id'] = author_login.id
            return 'Succseful login'
        else:
            return 'Password or email is not correct'

@app.route('/products')
def products():
    request_product = request.get_json()
    pass


if __name__=="__main__":
    app.run(debug=True)