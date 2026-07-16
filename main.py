## main.py
from copy import deepcopy
import seed_data

def load_recipes(): return seed_data.recipes
def load_inventory(): return deepcopy(seed_data.inventory)
def load_orders(): return seed_data.orders
def load_restock(): return seed_data.restock
def load_status(): return deepcopy(seed_data.status)

if __name__ == "__main__":
    print(f"Data Loaded: {len(load_recipes())} recipes.")

# Task 4

def find_recipe_by_name(recipe_data, item_name):
    """Finds a recipe by name. Returns the recipe dict or None if not found."""
    for recipe in recipe_data:
        if recipe["name"] == item_name:
            return recipe
    return None

def calculate_ingredient_requirements(recipe, quantity):
    """Calculates total grams needed for an order based on recipe and quantity."""
    requirements = []
    for ingredient in recipe["ingredients"]:
        requirements.append({
            "name": ingredient["name"],
            "required_qty_grams": ingredient["qty_grams"] * quantity
        })
    return requirements

# Task 5

def check_inventory_availability(inventory_data, requirements):
    """
    Checks if there is enough of each ingredient in stock.
    Returns: {"all_available": bool, "details": list}
    """
    availability_results = []
    all_available = True
    inventory_lookup = {item["ingredient"]: item for item in inventory_data}
    
    for req in requirements:
        inv_item = inventory_lookup.get(req["name"])
        available = inv_item["qty_grams"] if inv_item else 0
        is_enough = inv_item is not None and available >= req["required_qty_grams"]
        
        availability_results.append({
            "ingredient": req["name"],
            "is_available": is_enough,
            "available_qty": available
        })
        
        if not is_enough:
            all_available = False
    return {"all_available": all_available, "details": availability_results}

# Task 6

def deduct_inventory(inventory_data, requirements):
    """
    Deducts the required grams of each ingredient from the inventory.
    """
    inventory_lookup = {item["ingredient"]: item for item in inventory_data}
    for req in requirements:
        inv_item = inventory_lookup.get(req["name"])
        if inv_item:
            inv_item["qty_grams"] -= req["required_qty_grams"]

# Task 7

def process_all_orders(inventory_data, orders, recipes):
    """
    Processes a list of orders.
    Checks availability and deducts inventory if available.
    """
    for order in orders:
        recipe = find_recipe_by_name(recipes, order["item"])
        if not recipe:
            print(f"Recipe for {order['item']} not found.")
            continue
            
        requirements = calculate_ingredient_requirements(recipe, order["quantity"])
        availability = check_inventory_availability(inventory_data, requirements)
        
        if availability["all_available"]:
            deduct_inventory(inventory_data, requirements)
            print(f"Order {order['id']} processed successfully.")
        else:
            print(f"Order {order['id']} failed: Insufficient ingredients.")
        
# Task 8: Business Day Manager
def run_business_day(inventory, orders, recipes):
    """
    Simulates a full business day: processes all orders.
    """
    print("--- Starting Business Day ---")
    process_all_orders(inventory, orders, recipes)
    print("--- Business Day Complete ---")
    return inventory

# Task 9: Inventory Report
def generate_inventory_report(inventory):
    """Prints a clear summary of all ingredients and their current levels."""
    print("\n--- Current Inventory Status ---")
    for item in inventory:
        print(f"Ingredient: {item['ingredient']} | Stock: {item['qty_grams']}g")

# Task 10: Restock Logic
def check_and_restock(inventory, restock_data, threshold=500):
    """
    Checks if an ingredient is below the threshold and adds stock.
    """
    for item in inventory:
        if item["qty_grams"] < threshold:
            for r in restock_data:
                if r["ingredient"] == item["ingredient"]:
                    item["qty_grams"] += r["amount"]
                    print(f"Restocked {item['ingredient']} by {r['amount']}g.")