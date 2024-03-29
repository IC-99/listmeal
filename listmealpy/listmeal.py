import flask
from flask import request, render_template, redirect, flash, url_for
from my_calendar import MyCalendar
from my_kitchen import MyKitchen
from my_dictionary import MyDictionary
from my_shopping_list import MyShoppingList

LIST_MEAL = flask.Flask(__name__)
LIST_MEAL.secret_key = 'chiave segreta'
LIST_MEAL.config['SESSION_TYPE'] = 'filesystem'

MY_KITCHEN = MyKitchen()
MY_CALENDAR = MyCalendar()
MY_DICTIONARY = MyDictionary()
MY_SHOPPING_LIST = MyShoppingList(MY_CALENDAR, MY_KITCHEN)

LANGUAGE = "ita"

@LIST_MEAL.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': return render_template('index.html')
    
    return render_template('result.html')

@LIST_MEAL.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
    if request.method == 'GET': 
        return render_template('add_meal.html',
                               today=MY_CALENDAR.get_today_str(),
                               appetizers=MY_KITCHEN.get_category_names('appetizers'),
                               first_courses=MY_KITCHEN.get_category_names('first_courses'),
                               second_courses=MY_KITCHEN.get_category_names('second_courses'),
                               side_courses=MY_KITCHEN.get_category_names('side_courses'),
                               desserts=MY_KITCHEN.get_category_names('desserts'))
    
    date_name = request.form.get("date")
    meal_name = request.form.get("meal")
    appetizer_name = request.form.get("appetizer")
    if appetizer_name == 'Nessun antipasto': appetizer_name = ''
    first_course_name = request.form.get("first_course")
    if first_course_name == 'Nessun primo piatto': first_course_name = ''
    second_course_name = request.form.get("second_course")
    if second_course_name == 'Nessun secondo piatto': second_course_name = ''
    side_course_name = request.form.get("side_course")
    if side_course_name == 'Nessun contorno': side_course_name = ''
    dessert_name = request.form.get("dessert")
    if dessert_name == 'Nessun dolce': dessert_name = ''

    print(meal_name, appetizer_name, first_course_name, second_course_name, side_course_name, dessert_name)

    MY_CALENDAR.add_meal(date_name, meal_name, appetizer_name, first_course_name, second_course_name, side_course_name, dessert_name)
    return render_template('calendar.html', calendar_data=MY_CALENDAR.get_data(), dictionary=MY_DICTIONARY.get(LANGUAGE))

@LIST_MEAL.route('/recipe_catalogue', methods=['GET', 'POST'])
def recipe_catalogue():
    if request.method == 'GET': 
        return render_template('recipe_catalogue.html', catalogue_data=MY_KITCHEN.get_data(), dictionary=MY_DICTIONARY.get(LANGUAGE))

    return render_template('calendar.html', calendar_data=MY_CALENDAR.get_data(), dictionary=MY_DICTIONARY.get(LANGUAGE))

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

    return render_template('recipe_catalogue.html', catalogue_data=MY_KITCHEN.get_data(), dictionary=MY_DICTIONARY.get(LANGUAGE))     

@LIST_MEAL.route('/remove/<category>/<recipe_name>', methods=['GET'])
def remove_recipe(category, recipe_name):
    MY_KITCHEN.remove_recipe(category, recipe_name)
    return render_template('recipe_catalogue.html', catalogue_data=MY_KITCHEN.get_data(), dictionary=MY_DICTIONARY.get(LANGUAGE))

@LIST_MEAL.route('/remove_ingredient_form_recipe/<category>/<recipe_name>/<ingredient_name>', methods=['GET'])
def remove_ingredient_form_recipe(category, recipe_name, ingredient_name):
    MY_KITCHEN.remove_ingredient_form_recipe(category, recipe_name, ingredient_name)
    return render_template('recipe.html', recipe=MY_KITCHEN.get_recipe_dict(category, recipe_name), category=category, recipe_name=recipe_name)

@LIST_MEAL.route('/recipe/<category>/<recipe_name>', methods=['GET', 'POST'])
def recipe(category, recipe_name):
    if request.method == 'GET': 
        return render_template('recipe.html', recipe=MY_KITCHEN.get_recipe_dict(category, recipe_name), category=category, recipe_name=recipe_name)
    ingredient_name = request.form.get("ingredient_name")
    ingredient_amount = request.form.get("ingredient_amount")
    ingredient_unit = request.form.get("ingredient_unit")
    MY_KITCHEN.add_ingredient_to_recipe(category, recipe_name, ingredient_name, ingredient_amount, ingredient_unit)
    return render_template('recipe.html', recipe=MY_KITCHEN.get_recipe_dict(category, recipe_name), category=category, recipe_name=recipe_name)

@LIST_MEAL.route('/calendar', methods=['GET', 'POST'])
def calendar():
    if request.method == 'GET': 
        return render_template('calendar.html', calendar_data=MY_CALENDAR.get_data(), dictionary=MY_DICTIONARY.get(LANGUAGE))
    return render_template('index.html')

@LIST_MEAL.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list():
    if request.method == 'GET':
        return render_template('shopping_list.html', shopping_list_data=MY_SHOPPING_LIST.get_shopping_list(), dictionary=MY_DICTIONARY.get(LANGUAGE))
    return render_template('index.html')

if __name__ == '__main__':
    LIST_MEAL.run(debug=True, port=80, use_reloader=True)