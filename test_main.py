## test_main.py
import unittest
import main

class TestCloudKitchen(unittest.TestCase):
    def test_load_data(self):
        self.assertGreater(len(main.load_recipes()), 0)

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
        self.assertEqual(reqs[0]["required_qty_grams"], 600)

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

class TestOrderFulfillment(unittest.TestCase):
    def test_deduct_inventory(self):
        inventory = [{"ingredient": "Flour", "qty_grams": 500}]
        requirements = [{"name": "Flour", "required_qty_grams": 200}]
        main.deduct_inventory(inventory, requirements)
        self.assertEqual(inventory[0]["qty_grams"], 300)

class TestOrderProcessing(unittest.TestCase):
    def test_process_all_orders(self):
        inventory = [{"ingredient": "Flour", "qty_grams": 500}]
        recipes = [{"name": "Bread", "ingredients": [{"name": "Flour", "qty_grams": 200}]}]
        orders = [{"id": 1, "item": "Bread", "quantity": 1}, {"id": 2, "item": "Bread", "quantity": 1}]
        main.process_all_orders(inventory, orders, recipes)
        self.assertEqual(inventory[0]["qty_grams"], 100)

if __name__ == '__main__':
    unittest.main() 

# Task 8
class TestBusinessDay(unittest.TestCase):
    def test_run_business_day(self):
        inventory = [{"ingredient": "Flour", "qty_grams": 500}]
        recipes = [{"name": "Bread", "ingredients": [{"name": "Flour", "qty_grams": 200}]}]
        orders = [{"id": 1, "item": "Bread", "quantity": 1}]
        main.run_business_day(inventory, orders, recipes)
        self.assertEqual(inventory[0]["qty_grams"], 300)

# Task 9
class TestInventoryReport(unittest.TestCase):
    def test_generate_inventory_report(self):
        inventory = [{"ingredient": "Sugar", "qty_grams": 1000}]
        # We just verify it doesn't crash and prints the data
        try:
            main.generate_inventory_report(inventory)
            report_worked = True
        except:
            report_worked = False
        self.assertTrue(report_worked)