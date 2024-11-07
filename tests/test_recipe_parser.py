import unittest

from recipe_parser import import_recipes

class RecipeParserTest(unittest.TestCase):
    # Will run from script path so use as if it's running from top-level, not here
    data_path: str = "./data/recipes.json"

    def test_import_has_records(self):
        got: dict = import_recipes(self.data_path)
        want: int = 1

        self.assertGreaterEqual(len(got), want)
    
    def test_import_has_proper_shape(self):
        got: dict = import_recipes(self.data_path)

        self.assertEqual(type(got), list)

        for item in got:
            self.assertEqual(type(item), dict)
            
            self.assertIn("name", item)
            self.assertIn("ingredients", item)
            self.assertIn("instructions", item)

            self.assertEqual(type(item["name"]), str)
            self.assertEqual(type(item["ingredients"]), list)
            self.assertEqual(type(item["instructions"]), str)
