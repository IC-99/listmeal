from typing import List
import json

from recipe import Recipe
from ingredient_for_recipe import IngredientForRecipe

class RecipeCatalogue:
    
    def __init__(self) -> None:
        self.file_name = 'recipe_catalogue.json'
        self.catalogue = self.load_catalogue()

    def load_catalogue(self) -> List[dict]:
        f = open(self.file_name)
        catalogue = json.load(f)
        f.close()
        return catalogue
    
    def save_catalogue(self) -> None:
        json_object = json.dumps(self.catalogue, indent=2)
        with open(self.file_name, 'w') as out_file:
            out_file.write(json_object)
    
    def get_data(self) -> None:
        return self.catalogue

    def get_category(self, category: str) -> List[dict]:
        if category in self.catalogue:
            return self.catalogue[category]
        return []
    
    def get_recipe(self, category: str, name: str) -> dict:
        if category in self.catalogue:
            for recipe in self.catalogue[category]:
                if recipe['name'] == name:
                    return recipe
        return {}
    
    def get_recipe_by_name(self, name: str) -> dict:
        for category in self.catalogue:
            for recipe in self.catalogue[category]:
                if recipe["name"] == name:
                    return recipe
        return {}

    def add_recipe(self, recipe: Recipe) -> None:
        recipe_entry = {}
        recipe_entry['name'] = recipe.name
        recipe_entry['typology'] = recipe.typology
        recipe_entry['difficulty'] = recipe.difficulty
        recipe_entry['ingredients'] = []
        for ingredient in recipe.ingredients:
            ingredient_entry = {}
            ingredient_entry['name'] = ingredient.name
            ingredient_entry['amount'] = ingredient.amount
            ingredient_entry['unit'] = ingredient.unit
            recipe_entry['ingredients'].append(ingredient_entry)

        if not recipe.category in self.catalogue:
            self.catalogue[recipe.category] = []

        self.catalogue[recipe.category].append(recipe_entry)
        self.save_catalogue()

    def remove_recipe(self, category: str, name: str) -> None:
        if category in self.catalogue:
            for i in range(len(self.catalogue[category])):
                if self.catalogue[category][i]['name'] == name:
                    self.catalogue[category].pop(i)
                    self.save_catalogue()
                    return
                
    def add_ingredient_to_recipe(self, category: str, recipe_name: str, ingredient: IngredientForRecipe):
        ingredient_entry = {}
        ingredient_entry['name'] = ingredient.name
        ingredient_entry['amount'] = ingredient.amount
        ingredient_entry['unit'] = ingredient.unit
        if category in self.catalogue:
            for recipe in self.catalogue[category]:
                if recipe['name'] == recipe_name:
                    recipe['ingredients'].append(ingredient_entry)
            self.save_catalogue()
        
    def remove_ingredient_form_recipe(self, category: str, recipe_name: str, ingredient_name: str) -> None:
        if category in self.catalogue:
            for recipe in self.catalogue[category]:
                if recipe['name'] == recipe_name:
                    for i in range(len(recipe["ingredients"])):
                        if recipe["ingredients"][i]["name"] == ingredient_name:
                            recipe["ingredients"].pop(i)
                            self.save_catalogue()
                            return