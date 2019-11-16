from app import app, mongo
from flask import render_template, url_for


@app.route('/')
def home():
    #user_collection = mongo.db.user
    #user_collection.insert({'name': 'new1'})
    return render_template('home.html', title='Home')

@app.route('/guitar')
def guitar():
    return render_template('guitar.html', title='Guitar Tuner')
    
@app.route('/bass')
def bass():
    return render_template('bass.html', title='Bass Tuner')

@app.route('/drums')
def drums():
    return render_template('drums.html', title='Drums')