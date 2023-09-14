from typing import List
import json

from recipe import Recipe

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
    
    def get_category(self, category: str) -> List[dict]:
        if category in self.catalogue:
            return self.catalogue[category]
        return []

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
