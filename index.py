# importamos modulo de flask
from flask import Flask
from routes.Students import Estudiante
from routes.Administrativo import Administrativo
from routes.auth import auths
from routes.Documents import Documents
from flask_sqlalchemy import SQLAlchemy
from utils.config import DATABASE_URL

index = Flask(__name__)
files = index.config['UPLOAD_FOLDER'] = './Documents'


#settings
index.secret_key = 'mysecretkey'
index.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
# index.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://roignunqhvcqsm:ca8d1ec2b6ab18bf3e9cf1de52bb9e956a8aef7f1d7d0726e6f7a44a66cc9aad@ec2-3-219-204-29.compute-1.amazonaws.com:5432/d2ls4c3bb1ipt1'

index.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(index)


index.register_blueprint(Estudiante)
index.register_blueprint(Administrativo)
index.register_blueprint(auths)
index.register_blueprint(Documents)

