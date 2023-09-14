from ingredient import Ingredient

class IngredientForRecipe:

    def __init__(self, name: str, amount: str) -> None:
        self.name = name
        self.amount = amount

    def edit(self, ingredient: Ingredient, amount: str) -> None:
        self.ingredient = ingredient
        self.amount = amount