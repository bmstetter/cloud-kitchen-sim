### 3. `test_main.py`
import unittest
import main

class TestCloudKitchen(unittest.TestCase):
    def test_load_data(self):
        self.assertGreater(len(main.load_recipes()), 0)

if __name__ == '__main__':
    unittest.main()

# ... existing code ...

class TestRecipeLookup(unittest.TestCase):
    def test_find_recipe_exists(self):
        recipes = main.load_recipes()
        recipe = main.find_recipe_by_name(recipes, "Margherita Pizza")
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe["recipe_id"], 1)

    def test_calculate_ingredients(self):
        recipes = main.load_recipes()
        recipe = main.find_recipe_by_name(recipes, "Margherita Pizza")
        reqs = main.calculate_ingredient_requirements(recipe, 2)
        # 2 pizzas should need 600g flour (300*2)
        self.assertEqual(reqs[0]["required_qty_grams"], 600)

if __name__ == '__main__':
    unittest.main()