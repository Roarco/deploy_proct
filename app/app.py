# importamos modulo de flask
from flask import Flask
from routes.Student import students
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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)



app.register_blueprint(students)
app.register_blueprint(Administrativo)
app.register_blueprint(auths)
app.register_blueprint(Documents)
