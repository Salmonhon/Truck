from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from flask_marshmallow import Marshmallow



app = Flask(__name__)
app.config['SECRET_KEY'] = 'truck'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

api_cors_config = {
    'origins': ["http://localhost:5000"],
    'methods': ['POST', 'GET']
}
CORS(app, resources={
    r'/v1/*': api_cors_config
})

db = SQLAlchemy(app)
ma = Marshmallow(app)