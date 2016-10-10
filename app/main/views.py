from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/index2.html')
def index2():
    return render_template('index2.html')
