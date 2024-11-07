import unittest

from recipe_finder import find_recipes, extract_ingredients_from_input
from recipe_parser import import_recipes

class TestRecipeFinder(unittest.TestCase):
    data_path: str = "./data/recipes.json"
    recipes: list[dict]

    def setUp(self):
        self.recipes = import_recipes(self.data_path)

    def test_can_find_grilled_cheese_sandwich(self):
        grilled_cheese_ingredients: str = "butter, cheddar cheese, bread"

        ingredients: list[str] = extract_ingredients_from_input(grilled_cheese_ingredients)

        self.assertIn("butter", ingredients)
        self.assertIn("cheddar cheese", ingredients)
        self.assertIn("bread", ingredients)
        self.assertNotIn("broccoli", ingredients)

        got: list[dict] = find_recipes(ingredients, self.recipes)

        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["name"], "Grilled Cheese Sandwich")

    def test_can_not_find_tacos_with_partial_ingredient_list(self):
        taco_partial_ingredients: str = "ground beef, taco shells"

        ingredients: list[str] = extract_ingredients_from_input(taco_partial_ingredients)

        self.assertIn("ground beef", ingredients)
        self.assertIn("taco shells", ingredients)
        self.assertNotIn("lettuce", ingredients)

        got: list[dict] = find_recipes(ingredients, self.recipes)

        self.assertEqual(len(got), 0)

    def test_can_find_multiple_recipes(self):
        # Should cover grilled cheese and brusceta
        many_ingredients: str = "butter, cheddar cheese, bread, salt, oil"

        ingredients: list[str] = extract_ingredients_from_input(many_ingredients)

        self.assertIn("butter", ingredients)
        self.assertIn("cheddar cheese", ingredients)
        self.assertIn("bread", ingredients)
        self.assertIn("salt", ingredients)
        self.assertIn("oil", ingredients)
        self.assertNotIn("broccoli", ingredients)

        got: list[dict] = find_recipes(ingredients, self.recipes)

        self.assertEqual(len(got), 2)
        
        recipe_names: list[str] = [g["name"] for g in got]
        self.assertIn("Oil Brusceta", recipe_names)
        self.assertIn("Grilled Cheese Sandwich", recipe_names)
        self.assertNotIn("Stuffed Bell Peppers", recipe_names)