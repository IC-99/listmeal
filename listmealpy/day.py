import datetime

from meal import Meal

class Day:

    def __init__(self, day: int, month: int, year: int, meals: dict = {}) -> None:
        self.date = datetime.datetime(year, month, day)
        self.name = self.date.strftime("%A %d %B %Y")
        self.meals = meals

    def add_meal(self, name: str) -> bool:
        if name in self.meals:
            print('pasto già inserito')
            return False
        self.meals[name] = Meal(name)
        return True
    
    def get_meal(self, name: str) -> Meal:
        if name in self.meals:
            return self.meals[name]
        print('il pasto ', name, ' non esiste')
        return None
        