from flask import Flask, render_template ,url_for

app = Flask(__name__)

posts = [{'Author': 'John', 'Title': 'book1', 'Content': 'Sci fi', 'Date_Posted': 'April 20 2018'},
         {'Author': 'Ryan', 'Title': 'book2', 'Content': 'Action', 'Date_Posted': 'April 25 2018'}]


@app.route('/')
def home():
    return render_template('home.html', title="Home", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


if __name__ == "__main__":
    app.run(debug=True)
