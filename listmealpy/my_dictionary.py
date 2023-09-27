
class MyDictionary:
    def __init__(self) -> None:
        self.ita = {"lunch": "Pranzo", "dinner": "Cena", "appetizer": "Antipasto", "first_course": "Primo piatto", "second_course": "Secondo piatto", "side_course": "Contorno", "dessert": "Dolce"}

    def get(self, language: str):
        if language == 'ita':
            return self.ita