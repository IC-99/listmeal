from typing import List
from ingredient_for_recipe import IngredientForRecipe

class Recipe:

    def __init__(self,  name: str, category: str = '', typology: str = '', difficulty: str = '', ingredients: List[IngredientForRecipe] = []) -> None:
        self.name = name
        self.category = category
        self.typology = typology
        self.difficulty = difficulty
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: IngredientForRecipe):
        self.ingredients.append(ingredient)
