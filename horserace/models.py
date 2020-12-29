from datetime import datetime
from horserace import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class RaceData(db.Model):
    __tablename__ = 'race_data'
    race_data_id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    final_place = db.Column(db.Integer)
    pp = db.Column(db.Integer)
    horse_name = db.Column(db.String(50), nullable=False)
    jockey = db.Column(db.String(50), nullable=False)
    trainer = db.Column(db.String(50), nullable=False)
    win_odds = db.Column(db.Float)
    win_payout = db.Column(db.Float)
    place_payout = db.Column(db.Float)
    show_payout = db.Column(db.Float)
    year = db.Column(db.Integer)
    race = db.Column(db.String(50))
    high_temp = db.Column(db.Float)
    low_temp = db.Column(db.Float)
    precipitation = db.Column(db.Float)
    weather = db.Column(db.String(10), nullable=False)
    track_condition = db.Column(db.String(10), nullable=False)
    attendance = db.Column(db.Integer)

    def __init__(self, final_place, pp, horse_name, jockey, trainer, win_odds,
                 win_payout, place_payout, show_payout, year, race,high_temp, low_temp,
                 precipitation, weather, track_condition, attendance):
        # self.user_id = user_id
        self.final_place = final_place
        self.pp = pp
        self.horse_name = horse_name
        self.jockey = jockey
        self.trainer = trainer
        self.win_odds = win_odds
        self.win_payout = win_payout
        self.place_payout = place_payout
        self.show_payout = show_payout
        self.year = year
        self.race = race
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.precipitation = precipitation
        self.weather = weather
        self.track_condition = track_condition
        self.attendance = attendance






