from flask import (Flask, render_template, url_for, request)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # initializes

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zergling22!@localhost/triple-crown'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Race(db.Model):
    __tablename__ = 'race'
    raceId = db.Column(db.Integer, primary_key=True)
    conditionsId = db.Column(db.Integer)
    year = db.Column(db.Integer)
    race = db.Column(db.String(50))

    def __init__(self, conditionsId, year, race):
        self.conditionsId = conditionsId
        self.year = year
        self.race = race

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/recommend")
def recommend_view():
    return render_template("recommend.html")

@app.route("/table")
def table_view():
    return render_template("table.html")

@app.route("/about")
def about_view():
    return render_template("about.html")




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

if __name__ == '__main__':
    app.run()

