import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
#from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'coobkook'
app.config["MONGO_URI"] = 'mongodb://root:password123@ds121295.mlab.com:21295/coobkook'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('home.html', recipes = mongo.db.recipes.find())

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
    
    try:
        views = int(recipe['views'])
        views += 1
        recipe['views'] = views
        recipes = mongo.db.recipes
        recipes.update_one({"_id": ObjectId(recipe_id)},{ '$set': {'views':views}})
    except:
        recipes = mongo.db.recipes
        recipes.update_one({"_id": ObjectId(recipe_id)},{ '$set': {'views':'1'}})
    return render_template('showrecipe.html', recipe = recipe, counter=counter, ingredients = ingredient_list)
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisine=mongo.db.cuisine.find(), user=mongo.db.user.find(), allergen = mongo.db.allergens.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    if request.method == 'POST':
        result = request.form.to_dict()
        allergen_result = request.form.getlist('allergens')
        non_string = request.form.get('preparation')
        preparation_result = str(request.form.get('preparation'))
        preparation_string = preparation_result.split("\r\n")
        result['preparation'] = ', '.join(preparation_string)
        result['allergens'] = ', '.join(allergen_result)
        print(result['preparation'])
        print(type(result['preparation']))
        recipes = mongo.db.recipes
        recipes.insert_one(result)
    return redirect(url_for('list_recipes'))
    
    
@app.route('/search', methods=['POST', 'GET'])
def search():
    return render_template('search.html', recipes = mongo.db.recipes.find(), cuisine=mongo.db.cuisine.find(), user=mongo.db.user.find())

@app.route('/result', methods=['POST'])
def result():
    query = {}
    if request.method == 'POST':
        try:
            if request.form['user_name'] != 'None':
                user = request.form['user_name']
                query['user_name'] = user
        except:
            pass
        try:
            if request.form['cuisine_name']  != 'None':
                cuisine = request.form['cuisine_name']
                query['cuisine_name'] = cuisine
        except:
            pass
    print(query)
    search_result = mongo.db.recipes.find(query)
    
    return render_template('result.html', recipes = mongo.db.recipes.find(), search_result = search_result)
    
@app.route('/edit_recipe/<recipe_id>', methods=['POST', 'GET'])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredient_list = []
    ingredient_qty_list = []
    counter = int(recipe['ingredient_counter']) + 1
    for x in range(1, counter, 1):
        ingredient_list.append(recipe['ingredient_' + str(x)])
    for x in range(1, counter, 1):
        ingredient_qty_list.append(recipe['ingredient_qty_' + str(x)])
    return render_template('editrecipe.html', recipe = recipe, cuisine=mongo.db.cuisine.find(), user=mongo.db.user.find(), allergen = mongo.db.allergens.find(), ingredient_list = ingredient_list, ingredient_qty_list = ingredient_qty_list, counter = counter)
    
@app.route('/update_recipe/<recipe_id>/', methods=['POST', 'GET'])
def update_recipe(recipe_id):

    # maybe delete contents of recipe then add all like below?
    
    if request.method == 'POST':
        result = request.form.to_dict()
        allergen_result = request.form.getlist('allergens')
        non_string = request.form.get('preparation')
        preparation_result = str(request.form.get('preparation'))
        preparation_string = preparation_result.split("\r\n")
        result['preparation'] = ', '.join(preparation_string)
        result['allergens'] = ', '.join(allergen_result)
        recipes = mongo.db.recipes
        recipes.replace_one({"_id": ObjectId(recipe_id)}, result)
        return redirect(url_for('list_recipes'))
        #Figure out way to redirect back to same recipe ID
        
        # Something like: return redirect(url_for('show_recipe', recipe_id = this._id))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)