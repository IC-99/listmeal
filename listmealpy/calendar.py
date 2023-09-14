import datetime

from day import Day

class Calendar:

    def __init__(self, past: dict = {}, future: dict = {}) -> None:
        self.today = self.get_today()
        self.past = past
        self.future = future
        self.sort_calendar()
        self.update_calendar()

    def get_today(self) -> datetime.date:
        return datetime.datetime.now().date()

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
