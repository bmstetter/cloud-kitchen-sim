## main.py
from copy import deepcopy
from datetime import datetime
import seed_data

# --- DATA LOADERS ---
def load_recipes(): return seed_data.recipes
def load_inventory(): return deepcopy(seed_data.inventory)
def load_orders(): return seed_data.orders
def load_restock(): return seed_data.restock

# --- TASK 4: RECIPE MANAGEMENT ---
def find_recipe_by_name(recipe_data, item_name):
    for recipe in recipe_data:
        if recipe["name"] == item_name:
            return recipe
    return None

def calculate_ingredient_requirements(recipe, quantity):
    requirements = []
    for ingredient in recipe["ingredients"]:
        requirements.append({
            "name": ingredient["name"], 
            "required_qty_grams": ingredient["qty_grams"] * quantity
        })
    return requirements

# --- TASK 5: AVAILABILITY CHECK ---
def check_inventory_availability(inventory_data, requirements):
    all_available = True
    lookup = {item["ingredient"]: item for item in inventory_data}
    results = []
    for req in requirements:
        inv_item = lookup.get(req["name"])
        available = inv_item["qty_grams"] if inv_item else 0
        is_enough = inv_item is not None and available >= req["required_qty_grams"]
        results.append({"ingredient": req["name"], "is_available": is_enough})
        if not is_enough: all_available = False
    return {"all_available": all_available, "details": results}

# --- TASK 6: INVENTORY DEDUCTION ---
def deduct_inventory(inventory_data, requirements):
    lookup = {item["ingredient"]: item for item in inventory_data}
    for req in requirements:
        inv_item = lookup.get(req["name"])
        if inv_item: inv_item["qty_grams"] -= req["required_qty_grams"]

# --- TASK 7 & 8: ORDER PROCESSING (Updated for Nested Structure) ---
def process_all_orders(inventory_data, orders, recipes, status_list):
    """Processes orders with nested items, cumulative inventory, and status tracking."""
    for order in orders:
        for entry in order["items"]:
            recipe = find_recipe_by_name(recipes, entry["item"])
            if recipe:
                reqs = calculate_ingredient_requirements(recipe, entry["qty"])
                availability = check_inventory_availability(inventory_data, reqs)
                
                if availability["all_available"]:
                    deduct_inventory(inventory_data, reqs)
                    status_list.append({"order_id": order["order_id"], "delivered": True, "remark": "Delivered"})
                else:
                    reason = "Missing: " + ", ".join([d['ingredient'] for d in availability['details'] if not d['is_available']])
                    status_list.append({"order_id": order["order_id"], "delivered": False, "remark": reason})

# --- TASK 9 & 10: REPORTING & RESTOCK (Updated for New Keys) ---
def check_and_restock(inventory, restock_data, threshold=1000):
    today = datetime(2026, 7, 16)
    print("\n--- Restock & Expiry Report ---")
    for item in inventory:
        # Check Expiry
        expiry_date = datetime.strptime(item['expiry_date'], '%Y-%m-%d')
        days_until_expiry = (expiry_date - today).days
        if days_until_expiry <= 5:
            print(f"ALERT: {item['ingredient']} expiring in {days_until_expiry} days!")
        
        # Check Low Stock
        if item["qty_grams"] <= threshold:
            for r in restock_data:
                if r["item"] == item["ingredient"]:
                    print(f"RESTOCK: {item['ingredient']} is low ({item['qty_grams']}g). Replenishing by {r['qty_needed_grams']}g.")
                    item["qty_grams"] += r['qty_needed_grams']

def generate_inventory_report(inventory):
    print("\n--- Final Inventory Levels ---")
    for item in inventory:
        print(f"{item['ingredient']}: {item['qty_grams']}g")