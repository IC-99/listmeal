from ingredient import Ingredient

class IngredientForRecipe:

    def __init__(self, name: str, amount: str, unit: str) -> None:
        self.name = name
        self.amount = amount
        self.unit = unit

    def edit(self, ingredient: Ingredient, amount: str, unit: str) -> None:
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit