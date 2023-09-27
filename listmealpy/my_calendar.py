import datetime

from day import Day
from calendar_db import CalendarDb
from meal import Meal

class MyCalendar:

    def __init__(self, past: dict = {}, future: dict = {}) -> None:
        self.today = self.get_today()
        self.past = past
        self.future = future
        self.sort_calendar()
        self.update_calendar()
        self.calendar = CalendarDb()

    def get_today(self) -> datetime.date:
        return datetime.datetime.now().date()
    
    def get_today_str(self) -> str:
        return self.get_today().strftime("%Y-%m-%d")

    def sort_calendar(self) -> None:
        dict(sorted(self.past.items(), reverse=True))
        dict(sorted(self.future.items()))

    def is_past(self, date: datetime.date) -> bool:
        return date < self.today
    
    def update_calendar(self) -> None:
        self.today = self.get_today()
        for date in self.future.keys():
            if self.is_past(date):
                self.past[date] = self.future[date]
                del self.future[date]
            else:
                break
        self.sort_calendar()

    def add_day(self, day: int, month: int, year: int) -> bool:
        new_day = Day(day, month, year)
        self.today = self.get_today()
        if self.is_past(new_day.date):
            if new_day.date in self.past:
                print('giorno già inserito')
                return False
            else:
                self.past[new_day.date] = []
        else:
            if new_day.date in self.future:
                print('giorno già inserito')
                return False
            else:
                self.future[new_day.date] = []
        return True

    def add_meal(self, date_name: str, meal_name: str, appetizer_name: str, first_course_name: str, second_course_name: str, side_course_name: str, dessert_name: str) -> None:
        year = int(date_name[:4])
        month = int(date_name[5:7])
        day = int(date_name[8:])
        new_day = Day(day, month, year)
        new_meal = Meal(meal_name)

        new_meal.add_recipe_by_category_and_name('appetizer', appetizer_name)
        new_meal.add_recipe_by_category_and_name('first_course', first_course_name)
        new_meal.add_recipe_by_category_and_name('second_course', second_course_name)
        new_meal.add_recipe_by_category_and_name('side_course', side_course_name)
        new_meal.add_recipe_by_category_and_name('dessert', dessert_name)

        self.calendar.add_meal(new_day, new_meal)

    def get_data(self) -> dict:
        return self.calendar.get_data()
