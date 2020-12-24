from app import app
from flask import render_template


# If a user tries to browse to either no page (e.g. www.touro.edu/) or the index page, then call index() below
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home Page")


@app.route('/page2')
def page2():
    return render_template('page2.html', title="Page 2")


@app.route('/about')
def page3():
    return render_template('page3.html', title="About Page")
