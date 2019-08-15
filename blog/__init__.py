from flask import  Flask
from form import RegistrationForm, LogInForm
from flask_sqlalchemy import SQLAlchemy
from readfile import ReadFiles

file_read = ReadFiles('resource.properties')
app = Flask(__name__)
app.config['SECRET_KEY'] = '5ed6a070134958b4d5fcdfbd1e83e997'
app.config['SQLALCHEMY_DATABASE_URI'] = file_read.get_datalink()
db = SQLAlchemy(app)
