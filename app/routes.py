from app import app
from flask import request
@app.route('/')
def test():
    return 'Test!\n'

@app.route('/info', methods=['POST'])
def info():
    return request.json["temperature"]

