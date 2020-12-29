from flask import render_template, url_for, flash, redirect, request, session
from horserace.__init__ import app
from horserace.models import RaceData
import matplotlib as matplotlib
import cufflinks as cf
import pandas as pd
import json
import numpy as np

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        # check for user in db, place here
        if user and user.password == password:
            session['user_id'] = user.id

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

