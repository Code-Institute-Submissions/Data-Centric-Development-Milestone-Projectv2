

Installed Flask, flask-pymongo


https://stackoverflow.com/questions/21938788/jquery-function-before-form-submission


# Recipe Trove - Data Centric Development Project

The Recipe Trove website provides users the option to upload their favorite recipes on the website which includes ingredients and instructions in preparing them.
Website visitors can also view recipes from their favorite recipe uploader or by cuisine type using the search function.


The deployed project can be accessed on heroku at the following link: <a href="https://jan-data-centric-dev-project.herokuapp.com">Recipe Trove</a>

#

### **Table of Contents**

[User Experience](#user-experience)

[Features](#features)

[Features Left to Implement](#features-left-to-implement)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Deployment](#deployment)

#
 
### User Experience

As a user of the website, you need to be able to navigate through the uploaded recipes and upload your own.

The Recipe Trove site owners would like users to have the following experience on the website:
- Users need to get a taster of some recipes on the home page via the recipe carousel displaying a few features recipes
- Menu items should be displayed in the top right side of the page for navigation purposes
- All recipes should be displayed on the list recipes page
- Recipe entries should be clickable to open the individual recipe
- Search options allows to view recipes from specific users or by cuisine type
- Any user can create a recipe entry until user account management is implemented in the future
- On the recipe entry page, users need to be able to add ingredient rows based on the amount of recipe ingredients

#

### Features

- Home Page - Users get a peek of some featured recipes through a carousel displaying recipe images, recipe name and uploaders name
- List Recipes - Displays all recipes uploaded to the website. Shows the recipe image, recipe name, uploaders name and the option to view or edit the recipe
- Search - The search page gives the option to search recipes based on user (uploader) name and cuisine type
- Result - This page displays the results from the search options
- Add Recipe - Recipes can be added to the website on this page. Recipe username needs to be selected until authentication and user accounts are implemented

#

### Features Left to Implement

- User Authentication - Register, Login and Logout needs to be implemented. Add recipe page will then be updated to automatically select logged in users' details
- Pagination - Once recipe database grows in size, pagination needs to be implemented to limit the results being displayed per page
- Optional feature - Implement S3 storage that allows users to directly upload recipe images to website without first uploading on external image store.

#

### Technologies Used

- [HTML](https://www.w3.org/html/)
    - DOCTYPE of **HTML** is used for the markup of this project
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    - **CSS** used to style the project
- [JQuery](https://jquery.com)
    - The project uses **JQuery Version 3.3.1** to simplify DOM manipulation.
- [Materialize](https://materializecss.com/)
    - Using **Materialize 1.0.0** for front-end framework and website styling
- [PyMongo](https://api.mongodb.com/python/current/)
    - **PyMongo 3.7.2** used to work with MongoDB from Python
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - Providing the bridge between Flask and PyMongo, we use **Flask-PyMongo 2.2.0**
- [Flask](http://flask.pocoo.org/)
    - For the backend framework of this website, we utilise **Flask 1.0.2**

#

### Testing

Manual website testing was conducted to ensure the functionality of the site and the features are working as required. 

Testing conducted were as follows:

1. Home Page:
- Ensured that carousel is flipping between featured recipes and that the 'Show Recipes' button takes you to the recipe list page
- Clicking on the carousel entries flips to the next recipe in the featured list
- Tested menu bar buttons working except for Login and Register which still needs to be implemented

2. List Recipes:
- Accessed from the menu by clicking on the 'Show Recipes' button
- The list displays all the recipes that aren't deleted. Tested by deleting a recipe which removed it from the display
- Clicking on the recipe image or the "View or Edit Recipe" area opens up the selected recipe

3. Show Recipe:
- Opening up a recipe displays the recipe image, name, description, ingedients, preparation steps, recipe creator name, allergens and recipe views
- Clicking the 'Edit Recipe' button opens up the Edit Recipe page with the option to change the data of that recipe
- Clicking on the "Delete Recipe" button opens up the prompt to confirm deletion of the recipe
- Recipe Views increase every time the recipe is opened

4. Add Recipe:
- Cuisine Type, User Name and allergens pulls the correct information from the premade database selection options.
- Clicking the "Add Ingredient" and "Remove Ingredient" buttons works as expected
- The "Add Recipe" button saves the information in the database and displays the recipe in the recipe list page

5. Edit Recipe:
- Confirmed the dropdowns for Cuisine Type, User Name and allergens are working on the edit recipe page
- Can't remove ingredient if only 1 ingredient remains
- Adding an ingredient saves and displays
- Image change displays new image in recipe
- "Submit Change" button captures all the changes and retains all the unchanged items 

6. Delete Recipe:
- Clicking on the "Delete Recipe" button from the show recipe page, brings up a modal to confirm deletion
- Clicking "No" will return the user back to the show recipe page without deleting the recipe
- Selecting "Yes" will delete the recipe and direct the user back to the recipe list page

7. Search:
- Tested by searching by user, by cuisine type and by combining the search by user and type. Displays the correct recipes based on selections
- Clicking on a recipe from the search results opens up that recipe

8. Other:
- Login and Register buttons not functioning as they aren't implemented yet

9. Bugs discovered during testing:
- Add Recipe page - You can add a recipe without entering any information
- Edit Recipe page - You can edit a recipe and leave fields blank that should be required
- Show Recipe Page - Recipe default image (if no image was added during recipe creation) doesn't display, broken image icon shows


#

### Deployment

During the development phase and deployment, the project used MongoDB hosted on [mLab](https://mlab.com)

To desploy the project to Heroku, the following steps were taken:

- Created the application on Heroku and called it: jan-data-centric-dev-project
- Copied the MONGO_URI from the app.py and went to Settings on Heroku, then to Reveal Config Vars and entered the values there
- Changed the MONGO_URI entry in app.py to the following:
    - ```app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')```
- On my development environment, installed the webserver that is required by Heroku
    - ```pip install gunicorn```
- Create a Procfile file in the root of the project and add the following line to the file:
    - ```web: gunicorn app:app```
- Capture all the installed applications into the requirements.txt file:
    - ```pip freeze > requirements.txt```


### Credits

**Content**


**Media** 


**Code**


**Inspiration**
