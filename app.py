import os
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = ''

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)