from flask import render_template, url_for, flash, redirect

from models import Post, User

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
