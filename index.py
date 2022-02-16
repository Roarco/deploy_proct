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
# index.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
index.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mftfkdpetpjckm:4aa7070a1b03863fa6019ad0ceed99aa892f6e2747314dc46400acf419218ee5@ec2-52-45-83-163.compute-1.amazonaws.com:5432/dfh6e8prkc1jb2'
index.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(index)


index.register_blueprint(Estudiante)
index.register_blueprint(Administrativo)
index.register_blueprint(auths)
index.register_blueprint(Documents)

