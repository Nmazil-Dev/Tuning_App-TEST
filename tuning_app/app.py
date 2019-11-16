from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nic:pass1@cluster0-xqvdu.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def home():
    user_collection = mongo.db.user
    user_collection.insert({'name': 'new1'})
    return "New user added"

if __name__ == '__main__':
    app.run(debug=True)