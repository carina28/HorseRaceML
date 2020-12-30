from flask import render_template, url_for, flash, redirect, request, session
from horserace.__init__ import app
from horserace import db
from flask_sqlalchemy import SQLAlchemy
from horserace.models import User
from horserace.models import RaceData
import matplotlib as matplotlib
import pandas as pd
import numpy as np

app.secret_key = 'somethingSecret'


@app.route("/login", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def login():
    global db_username, db_password
    if request.method == 'POST':
        # session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        db_user = User.query.filter_by(username=username).first()

        if db_user is not None:
            db_username = db_user.username
            db_password = db_user.password

            if username == db_username and password == db_password:
                return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))

    return render_template("informational/login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("analytical/dashboard.html")


@app.route("/recommend")
def recommend_view():
    return render_template("analytical/recommend.html")


@app.route("/about")
def about_view():
    return render_template("informational/about.html")

# @app.route("/logout")
# def logout():
#     return render_template("informational/login.html")