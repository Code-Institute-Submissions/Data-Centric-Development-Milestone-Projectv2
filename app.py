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
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredient_list = []
    counter = int(recipe['ingredient_counter']) + 1
    for x in range(1, counter, 1):
        ingredient_list.append(recipe['ingredient_' + str(x)] + ': ' + recipe['ingredient_qty_' + str(x)])
    
    return render_template('showrecipe.html', recipe = recipe, counter=counter, ingredients = ingredient_list)
    
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