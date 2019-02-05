import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
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
    
@app.route('/show_recipe/<recipe_id>/')
def show_recipe(recipe_id):
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    entries = recipe_id.items()
    
    return render_template('showrecipe.html', entries = entries)
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisine=mongo.db.cuisine.find(), user=mongo.db.user.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    print(request.form)
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('list_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)