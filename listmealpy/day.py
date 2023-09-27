import datetime

from meal import Meal

class Day:

    def __init__(self, day: int, month: int, year: int) -> None:
        self.date = datetime.datetime(year, month, day)
        self.name = self.date.strftime("%A %d %B %Y")
        self.key = self.date.strftime("%Y-%m-%d")
        