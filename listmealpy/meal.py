from typing import List

from recipe import Recipe

class Meal:

    def __init__(self, name: str, recipes: List[Recipe] = []) -> None:
        self.name = name
        self.recipes = recipes

    def add_course(self, recipe: Recipe):
        self.recipes.append(recipe)