from typing import List

from recipe import Recipe

class Meal:

    def __init__(self, name: str, recipes: dict = {}) -> None:
        self.name = name
        self.recipes = recipes

    def add_recipe(self, recipe: Recipe) -> None:
        self.recipes[recipe.category] = recipe.name

    def add_recipe_by_category_and_name(self, category: str, name: str) -> None:
        self.recipes[category] = name