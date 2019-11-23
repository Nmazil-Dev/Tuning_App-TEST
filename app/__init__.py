from flask import Flask, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nic:pass1@cluster0-xqvdu.mongodb.net/tuningapp?retryWrites=true&w=majority"
mongo = PyMongo(app)

app = Flask(__name__)

from app import routes