# importamos modulo de flask
from flask import Flask
from routes.Students import Estudiante
from routes.Administrativo import Administrativo
from routes.auth import auths
from routes.Documents import Documents
from flask_sqlalchemy import SQLAlchemy
from utils.config import DATABASE_URL


app = Flask(__name__)
files = app.config['UPLOAD_FOLDER'] = '../Documents'


#settings
app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://roignunqhvcqsm:ca8d1ec2b6ab18bf3e9cf1de52bb9e956a8aef7f1d7d0726e6f7a44a66cc9aad@ec2-3-219-204-29.compute-1.amazonaws.com:5432/d2ls4c3bb1ipt1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)


app.register_blueprint(Estudiante)
app.register_blueprint(Administrativo)
app.register_blueprint(auths)
app.register_blueprint(Documents)
