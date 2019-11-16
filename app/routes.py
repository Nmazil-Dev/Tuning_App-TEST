from app import app, mongo
from flask import render_template, url_for


@app.route('/')
def index():
    #user_collection = mongo.db.user
    #user_collection.insert({'name': 'new1'})
    return render_template('home.html', title='Home')