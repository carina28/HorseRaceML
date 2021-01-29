from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__) # initializes


ENV = 'dev'
app.static_folder = 'static'


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zergling22!@localhost/triple-crown'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from horserace import routes