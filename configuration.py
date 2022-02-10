from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail



app = Flask(__name__)
app.config['SECRET_KEY'] = 'truck'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy(app)