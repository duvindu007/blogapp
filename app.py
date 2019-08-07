from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LogInForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ed6a070134958b4d5fcdfbd1e83e997'

posts = [{'Author': 'John', 'Title': 'book1', 'Content': 'Sci fi', 'Date_Posted': 'April 20 2018'},
         {'Author': 'Ryan', 'Title': 'book2', 'Content': 'Action', 'Date_Posted': 'April 25 2018'}]


@app.route('/')
def home():
    return render_template('home.html', title="Home", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm();
    if form.validate():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('registration.html', title='Registraion', form=form)


@app.route('/logIn')
def login():
    form = LogInForm();
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
