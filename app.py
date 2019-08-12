from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LogInForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from readfile import readFiles

file_read = readFiles()
file_read.readproperties('resource.properties')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ed6a070134958b4d5fcdfbd1e83e997'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/blog'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), unique=True, nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


posts = [{'Author': 'John', 'Title': 'book1', 'Content': 'Sci fi', 'Date_Posted': 'April 20 2018'},
         {'Author': 'Ryan', 'Title': 'book2', 'Content': 'Action', 'Date_Posted': 'April 25 2018'}]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('registration.html', title='Registraion', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
