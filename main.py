### 2. `main.py` 
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
    
    # Create a lookup dictionary for ingredients
    inventory_lookup = {item["ingredient"]: item for item in inventory_data}
    
    for req in requirements:
        inv_item = inventory_lookup.get(req["name"])
        # If the item doesn't exist in inventory, treat available as 0
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
``