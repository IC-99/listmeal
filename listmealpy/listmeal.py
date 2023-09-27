import flask
from flask import request, render_template, redirect, flash, url_for
from my_calendar import MyCalendar
from my_kitchen import MyKitchen

LIST_MEAL = flask.Flask(__name__)
LIST_MEAL.secret_key = 'chiave segreta'
LIST_MEAL.config['SESSION_TYPE'] = 'filesystem'

MY_CALENDAR = MyCalendar()
MY_KITCHEN = MyKitchen()

@LIST_MEAL.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': return render_template('index.html')
    
    return render_template('result.html')

@LIST_MEAL.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
    if request.method == 'GET': 
        return render_template('add_meal.html',
                               today=MY_CALENDAR.get_today_str(),
                               appetizers=MY_KITCHEN.get_category_names('appetizer'),
                               first_courses=MY_KITCHEN.get_category_names('first_course'),
                               second_courses=MY_KITCHEN.get_category_names('second_course'),
                               side_courses=MY_KITCHEN.get_category_names('side_course'),
                               desserts=MY_KITCHEN.get_category_names('dessert'))

    return render_template('result.html')

@LIST_MEAL.route('/recipe_catalogue', methods=['GET', 'POST'])
def recipe_catalogue():
    if request.method == 'GET': 
        return render_template('recipe_catalogue.html',
                               appetizers=MY_KITCHEN.get_category('appetizer'),
                               first_courses=MY_KITCHEN.get_category('first_course'),
                               second_courses=MY_KITCHEN.get_category('second_course'),
                               side_courses=MY_KITCHEN.get_category('side_course'),
                               desserts=MY_KITCHEN.get_category('dessert'))

    return render_template('result.html')

@LIST_MEAL.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'GET': 
        return render_template('add_recipe.html')

    recipe_name = request.form.get("recipe_name")
    recipe_category = request.form.get("recipe_category")
    recipe_typology = request.form.get("recipe_typology")
    recipe_difficulty = request.form.get("recipe_difficulty")
    recipe_ingredients = []
    MY_KITCHEN.add_recipe(recipe_name, recipe_category, recipe_typology, recipe_difficulty, recipe_ingredients)

    return render_template('recipe_catalogue.html',
                            appetizers=MY_KITCHEN.get_category('appetizer'),
                            first_courses=MY_KITCHEN.get_category('first_course'),
                            second_courses=MY_KITCHEN.get_category('second_course'),
                            side_courses=MY_KITCHEN.get_category('side_course'),
                            desserts=MY_KITCHEN.get_category('dessert'))      

@LIST_MEAL.route('/remove/<category>/<recipe_name>', methods=['GET'])
def remove_recipe(category, recipe_name):
    MY_KITCHEN.remove_recipe(category, recipe_name)
    return render_template('recipe_catalogue.html',
                               appetizers=MY_KITCHEN.get_category('appetizer'),
                               first_courses=MY_KITCHEN.get_category('first_course'),
                               second_courses=MY_KITCHEN.get_category('second_course'),
                               side_courses=MY_KITCHEN.get_category('side_course'),
                               desserts=MY_KITCHEN.get_category('dessert'))

@LIST_MEAL.route('/recipe/<category>/<recipe_name>', methods=['GET', 'POST'])
def recipe(category, recipe_name):
    if request.method == 'GET': 
        return render_template('recipe.html', recipe=MY_KITCHEN.get_recipe(category, recipe_name), category=category, recipe_name=recipe_name)
    ingredient_name = request.form.get("ingredient_name")
    ingredient_amount = request.form.get("ingredient_amount")
    ingredient_unit = request.form.get("ingredient_unit")
    MY_KITCHEN.add_ingredient_to_recipe(category, recipe_name, ingredient_name, ingredient_amount, ingredient_unit)
    return render_template('recipe.html', recipe=MY_KITCHEN.get_recipe(category, recipe_name), category=category, recipe_name=recipe_name)

if __name__ == '__main__':
    LIST_MEAL.run(debug=True, port=80, use_reloader=True)