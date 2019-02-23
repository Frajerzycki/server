from app import app, db
from flask import request, render_template, url_for
from tinydb.storages import JSONStorage
from datetime import datetime
import time
@app.route('/')
def test():
    return 'Test!\n'

@app.route('/info', methods=['POST'])
def info():
    data = request.json
    data['id'] = int(round(time.time() * 1000))
    db.insert(data)
    return request.json["temperature"]

@app.route("/weather")
def weather():
    return render_template('weather.html', w=db.all(),datetime=datetime, int=int)