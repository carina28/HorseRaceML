from flask import (Flask, render_template, url_for)

app = Flask(__name__)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")