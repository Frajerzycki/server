from flask import Flask
from tinydb import TinyDB
from tinydb.middlewares import CachingMiddleware
app = Flask(__name__)
db = TinyDB("data.json")
from app import routes
