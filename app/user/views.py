from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import user


@user.route('/')
def index():
    if current_user.is_anonymous :
        return redirect(url_for('main.index'))
    return render_template('user/index.html')
