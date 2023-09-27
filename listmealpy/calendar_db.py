from typing import List
import json

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

    def add_meal(self, day: str, meal: Meal) -> None:
        if not day in self.calendar:
            new_day = {}
            new_day[meal.name] = meal.recipes.copy()
            self.calendar[day] = new_day
        else:
            new_day = self.calendar[day].copy()
            new_day[meal.name] = meal.recipes.copy()
            self.calendar[day] = new_day
        self.save_calendar()

    def get_data(self) -> dict:
        return self.calendar