import datetime

class MyCalendar:

    def __init__(self, past: dict = {}, future: dict = {}) -> None:
        self.today = self.get_today()

    def get_today(self) -> datetime.date:
        return datetime.datetime.now().date()
    
    def get_today_str(self) -> str:
        return self.get_today().strftime("%Y-%m-%d")
    

calendar = MyCalendar()
print(calendar.get_today_str())