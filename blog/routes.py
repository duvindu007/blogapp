from flask import render_template, url_for, flash, redirect
from blog.form import RegistrationForm, LogInForm
from blog import app, db, b_crypt
from blog.models import Post, User
from flask_login import login_user, current_user, logout_user , login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_password = b_crypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(user_name=form.username.data, email=form.email.data, password=hased_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has created! you can now login!', 'success')
        return redirect(url_for('home'))

    return render_template('registration.html', title='Registraion', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and b_crypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
