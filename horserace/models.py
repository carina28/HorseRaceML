from datetime import datetime
from horserace import db

class Horse(db.Model):
    __tablename__ = 'horse'
    horse_id = db.Column(db.Integer, primary_key=True)
    horse_name = db.Column(db.String(50), nullable=False)
    jockey = db.Column(db.String(50), nullable=False)
    trainer = db.Column(db.String(50), nullable=False)

    def __init__(self, horse_name, jockey, trainer):
        self.horse_name = horse_name
        self.jockey = jockey
        self.trainer = trainer

class Conditions(db.Model):
    __tablename__ = 'conditions'
    conditions_id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'), nullable=False)
    high_temp = db.Column(db.Float)
    low_temp = db.Column(db.Float)
    precipitation = db.Column(db.Float)
    weather = db.Column(db.String(10), nullable=False)
    track_condition = db.Column(db.String(10), nullable=False)
    attendance = db.Column(db.Integer)

    def __init__(self, race_id, high_temp, low_temp, precipitation, weather, track_condition,
                 attendance):
        self.race_id = race_id
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.precipitation = precipitation
        self.weather = weather
        self.track_condition = track_condition
        self.attendance = attendance


class Race(db.Model):
    __tablename__ = 'race'
    race_id = db.Column(db.Integer, primary_key=True)
    conditions_id = db.Column(db.Integer, db.ForeignKey('conditions.conditions_id'))
    year = db.Column(db.Integer)
    race = db.Column(db.String(50))

    def __init__(self, conditions_id, year, race):
        self.conditions_id = conditions_id
        self.year = year
        self.race = race


class Results(db.Model):
    __tablename__ = 'results'
    result_id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'), nullable=False)
    horse_id = db.Column(db.Integer, db.ForeignKey('horse.horse_id'))
    pp = db.Column(db.Integer)
    final_place = db.Column(db.Integer)
    win_odds = db.Column(db.Float)
    win_payout = db.Column(db.Float)
    place_payout = db.Column(db.Float)
    show_payout = db.Column(db.Float)

    def __init__(self, race_id, horse_id, pp, final_place, win_odds, win_payout, place_payout,
                 show_payout):
        self.race_id = race_id
        self.horse_id = horse_id
        self.pp = pp
        self.final_place = final_place
        self.win_odds = win_odds
        self.win_payout = win_payout
        self.place_payout = place_payout
        self.show_payout = show_payout


