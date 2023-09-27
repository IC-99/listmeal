from typing import List
import json

from day import Day
from ingredient_for_recipe import IngredientForRecipe
from meal import Meal

class CalendarDb:
    
    def __init__(self) -> None:
        self.file_name = 'calendar_db.json'
        self.calendar = self.load_clendar()

    def load_clendar(self) -> List[dict]:
        f = open(self.file_name)
        calendar = json.load(f)
        f.close()
        return calendar
    
    def save_calendar(self) -> None:
        json_object = json.dumps(self.calendar, indent=2)
        with open(self.file_name, 'w') as out_file:
            out_file.write(json_object)
    
    def get_day(self, day: str) -> List[dict]:
        if day in self.calendar:
            return self.calendar[day]
        return []
    
    def get_meal(self, day: str, meal_name: str) -> dict:
        if day in self.calendar:
            for meal in self.calendar[day]:
                if meal['name'] == meal_name:
                    return meal
        return {}

    def add_meal(self, day: Day) -> None:
        date = day.key
        if not date in self.calendar:
            new_day = {}
            for meal in day.meals.keys():
                meal_entry = {}
                for category in day.meals[meal].recipes.keys():
                    meal_entry[category] = day.meals[meal].recipes[category].name
                new_day[meal] = meal_entry
            self.calendar[date] = new_day
        else:
            new_day = self.calendar[date]
            for meal in day.meals.keys():
                meal_entry = {}
                for category in day.meals[meal].recipes.keys():
                    meal_entry[category] = day.meals[meal].recipes[category].name
                new_day[meal] = meal_entry
            self.calendar[date] = new_day
        self.save_calendar()
