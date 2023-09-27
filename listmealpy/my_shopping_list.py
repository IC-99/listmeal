from my_calendar import MyCalendar
from my_kitchen import MyKitchen

class MyShoppingList:

    def __init__(self, calendar: MyCalendar, kitchen: MyKitchen) -> None:
        self.calendar = calendar
        self.kitchen = kitchen
        self.shopping_list = self.calculate()

    def calculate(self) -> None:
        self.shopping_list = {}
        future_recipes = self.calendar.get_future_recipes()
        for future_recipe in future_recipes:
            future_recipe_dict = self.kitchen.get_recipe_dict_by_name(future_recipe)
            for ingredient in future_recipe_dict["ingredients"]:
                ingredient_name = ingredient["name"]
                ingredient_amount = int(ingredient["amount"]) * future_recipes[future_recipe]
                ingredient_unit = ingredient["unit"]
                if ingredient_name in self.shopping_list:
                    amount, unit = self.shopping_list[ingredient_name]
                    if unit == ingredient_unit:
                        amount += ingredient_amount
                        self.shopping_list[ingredient_name] = (amount, unit)
                    else:
                        pass
                else:
                    self.shopping_list[ingredient_name] = (ingredient_amount, ingredient_unit)
        
    def get_shopping_list(self) -> dict:
        self.calculate()
        return self.shopping_list

