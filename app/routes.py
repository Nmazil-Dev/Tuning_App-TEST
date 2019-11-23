from app import app, mongo
from flask import render_template, url_for

#TODO Add to utils.py and import to routes
def get_strings(instrument, tuning):
    instrument_col = mongo.db[instrument]
    x = instrument_col.find({'tuning': tuning}, {"_id": 0, "tuning": 0 })
    string_list = []
    for doc in x:
        strings = (doc['strings'])
    strings = strings.values()
    return strings

def get_tunings(instrument):
    instrument_col = mongo.db[instrument]
    x = instrument_col.find({}, {"_id": 0, "strings": 0})
    tunings = []
    for doc in x:
        tunings.append(doc['tuning'])
    return tunings


@app.route('/')
def home():
    #user_collection = mongo.db.user
    #user_collection.insert({'name': 'new1'})
    return render_template('home.html', title='Home')

@app.route('/guitar')
def guitar():
    tunings = get_tunings('guitar')
    # TODO Get the tuning from the tunings dropdown and pass to get_strings()
    strings = get_strings('guitar', "Standard")
    return render_template('guitar.html', title='Guitar Tuner', tunings=tunings, strings=strings)
    
@app.route('/bass')
def bass():
    tunings = get_tunings('bass')
    # TODO Get the tuning from the tunings dropdown and pass to get_strings()
    strings = get_strings('bass', "Standard")
    return render_template('bass.html', title='Bass Tuner', tunings=tunings, strings=strings)

@app.route('/drums')
def drums():
    return render_template('drums.html', title='Drums')

@app.route('/shred')
def shred():
    return render_template('shred.html', title="Songs")