from flask import render_template, url_for, flash, redirect, request
from horserace.__init__ import app
from horserace.models import Horse, Conditions, Race, Results

@app.route("/")
# @app.route("/dashboard")
def dashboard():
    return render_template("analytical/dashboard.html")

@app.route("/recommend")
def recommend_view():
    return render_template("analytical/recommend.html")

@app.route("/table")
def table_view():
    return render_template("informational/table.html")

@app.route("/about")
def about_view():
    return render_template("informational/about.html")


@app.route('/go-dates', methods=['POST'])
def go_dates():
    if request.method == 'POST':
        year_start = request.form['year-select-start']
        year_end = request.form['year-select-end']
        # print(year_start, year_end)
        if year_start > year_end:
            return render_template('dashboard.html',
                                   message='Start year cannot be greater than end year.')
        # if year_start <= year_end:
        #     db.session.query(Race).filter(Race.year == year_start).count() # example sql execution, change
        #     data = Race(year_start, year_end)
        return render_template("about.html")

@app.route('/submit-rec', methods=['POST'])
def submit_rec():
    if request.method == 'POST':
        year_start = request.form['rec-year-start']
        year_end = request.form['rec-year-end']
        if year_start > year_end:
            return render_template('recommendation.html ')