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

# ... existing code ...

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
``