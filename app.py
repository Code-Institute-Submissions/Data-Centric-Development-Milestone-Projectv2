import os
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'coobkook'
app.config["MONGO_URI"] = 'mongodb://root:password123@ds121295.mlab.com:21295/coobkook'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/list_recipes')
def list_recipes():
    return render_template('listrecipes.html', recipes = mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)