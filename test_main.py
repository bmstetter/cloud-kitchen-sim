## test_main.py
import unittest
import main

class TestCloudKitchen(unittest.TestCase):

    def test_find_recipe(self):
        recipes = [{"name": "Burger", "recipe_id": 1, "ingredients": []}]
        self.assertIsNotNone(main.find_recipe_by_name(recipes, "Burger"))

    def test_calculate_reqs(self):
        recipe = {"ingredients": [{"name": "Bun", "qty_grams": 100}]}
        reqs = main.calculate_ingredient_requirements(recipe, 2)
        self.assertEqual(reqs[0]["required_qty_grams"], 200)

    def test_check_availability(self):
        inv = [{"ingredient": "Bun", "qty_grams": 50}]
        reqs = [{"name": "Bun", "required_qty_grams": 100}]
        self.assertFalse(main.check_inventory_availability(inv, reqs)["all_available"])

    def test_deduct(self):
        inv = [{"ingredient": "Bun", "qty_grams": 500}]
        reqs = [{"name": "Bun", "required_qty_grams": 100}]
        main.deduct_inventory(inv, reqs)
        self.assertEqual(inv[0]["qty_grams"], 400)

    # UPDATED: Now uses nested order structure
    def test_process_orders(self):
        inv = [{"ingredient": "Bun", "qty_grams": 500, "expiry_date": "2026-07-20"}]
        recipes = [{"name": "Burger", "ingredients": [{"name": "Bun", "qty_grams": 100}]}]
        orders = [{"order_id": 1, "items": [{"item": "Burger", "qty": 2}]}]
        status = []
        main.process_all_orders(inv, orders, recipes, status)
        self.assertEqual(inv[0]["qty_grams"], 300)
        self.assertTrue(status[0]["delivered"])

    # UPDATED: Now uses nested order structure
    def test_restock(self):
        inv = [{"ingredient": "Bun", "qty_grams": 100, "expiry_date": "2026-07-20"}]
        restock = [{"item": "Bun", "qty_needed_grams": 500}]
        main.check_and_restock(inv, restock, threshold=200)
        self.assertEqual(inv[0]["qty_grams"], 600)

if __name__ == '__main__':
    unittest.main()