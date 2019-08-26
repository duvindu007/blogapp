from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.readfile import ReadFiles
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

file_read = ReadFiles('resource.properties')
app = Flask(__name__)
app.config['SECRET_KEY'] = '5ed6a070134958b4d5fcdfbd1e83e997'
app.config['SQLALCHEMY_DATABASE_URI'] = file_read.get_datalink()
db = SQLAlchemy(app)
b_crypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from blog import routes
