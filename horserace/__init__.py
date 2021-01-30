from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

app = Flask(__name__) # initializes
db = SQLAlchemy(app)

# ENV = 'dev'
app.static_folder = 'static'
app.debug = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zergling22!@localhost/triple-crown'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yipfhhdxmzkbkh:393c7f6e2f463b863fd761bf12b66107e97da542a72c1a839fd5f41b0da2d9be@ec2-3-220-23-212.compute-1.amazonaws.com:5432/de9v3q9972n38b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



from horserace import routes