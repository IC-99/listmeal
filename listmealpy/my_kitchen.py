from typing import List

from recipe_catalogue import RecipeCatalogue
from ingredient_for_recipe import IngredientForRecipe
from recipe import Recipe


class MyKitchen:

    def __init__(self) -> None:
        self.recipe_catalogue = RecipeCatalogue()

    def get_category_names(self, category: str) -> List[str]:
        category_names = []
        for recipe in self.recipe_catalogue.get_category(category):
            category_names.append(recipe["name"])
        return category_names

    def get_category(self, category: str) -> List[dict]:
        return self.recipe_catalogue.get_category(category)
    
    def add_recipe(self, name: str, category: str, typology: str, difficulty: str, ingredients: List) -> None:
        recipe = Recipe(name, category, typology, difficulty, [])
        for ingredient_name, ingredient_amount, ingredient_unit in ingredients:
            ingredient = IngredientForRecipe(ingredient_name, ingredient_amount, ingredient_unit)
            recipe.add_ingredient(ingredient)
        self.recipe_catalogue.add_recipe(recipe)