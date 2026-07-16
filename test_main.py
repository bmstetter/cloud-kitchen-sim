## test_main.py
import unittest
import main

class TestCloudKitchen(unittest.TestCase):
    def test_load_data(self):
        self.assertGreater(len(main.load_recipes()), 0)

# Task 4

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

# Task 5

class TestInventoryAvailability(unittest.TestCase):
    def test_check_inventory_availability_success(self):
        inventory = [{"ingredient": "Flour", "qty_grams": 500}]
        requirements = [{"name": "Flour", "required_qty_grams": 200}]
        result = main.check_inventory_availability(inventory, requirements)
        self.assertTrue(result["all_available"])

    def test_check_inventory_availability_failure(self):
        inventory = [{"ingredient": "Flour", "qty_grams": 100}]
        requirements = [{"name": "Flour", "required_qty_grams": 200}]
        result = main.check_inventory_availability(inventory, requirements)
        self.assertFalse(result["all_available"])
        self.assertFalse(result["details"][0]["is_available"])

if __name__ == '__main__':
    unittest.main()

# Task 6

class TestOrderFulfillment(unittest.TestCase):
    def test_deduct_inventory(self):
        inventory = [{"ingredient": "Flour", "qty_grams": 500}]
        requirements = [{"name": "Flour", "required_qty_grams": 200}]
        main.deduct_inventory(inventory, requirements)
        # 500 - 200 should leave 300
        self.assertEqual(inventory[0]["qty_grams"], 300)

if __name__ == '__main__':
    unittest.main()