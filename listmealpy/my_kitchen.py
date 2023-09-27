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
    
    def get_recipe_dict(self, category: str, name: str) -> dict:
        return self.recipe_catalogue.get_recipe(category, name)
    
    def get_recipe(self, category: str, name: str) -> Recipe:
        dict_recipe = self.get_recipe_dict(category, name)
        recipe = Recipe(dict_recipe["name"], category, dict_recipe["typology"], dict_recipe["difficulty"], [])
        for ingredient_name, ingredient_amount, ingredient_unit in dict_recipe["ingredients"]:
            ingredient = IngredientForRecipe(ingredient_name, ingredient_amount, ingredient_unit)
            recipe.add_ingredient(ingredient)
        return recipe

    def add_recipe(self, name: str, category: str, typology: str, difficulty: str, ingredients: List) -> None:
        recipe = Recipe(name, category, typology, difficulty, [])
        for ingredient_name, ingredient_amount, ingredient_unit in ingredients:
            ingredient = IngredientForRecipe(ingredient_name, ingredient_amount, ingredient_unit)
            recipe.add_ingredient(ingredient)
        self.recipe_catalogue.add_recipe(recipe)

    def add_ingredient_to_recipe(self, category: str, recipe_name: str, ingredient_name: str, ingredient_amount: str, ingredient_unit: str) -> None:
        ingredient = IngredientForRecipe(ingredient_name, ingredient_amount, ingredient_unit)
        self.recipe_catalogue.add_ingredient_to_recipe(category, recipe_name, ingredient)

    def remove_recipe(self, category: str, name: str) -> None:
        self.recipe_catalogue.remove_recipe(category, name)

    def remove_ingredient_form_recipe(self, category: str, recipe_name: str, ingredient_name: str) -> None:
        self.recipe_catalogue.remove_ingredient_form_recipe(category, recipe_name, ingredient_name)