import seed_data

def display_data_structures():
    """
    Loads and prints the major data structures from seed_data.py
    to verify format and accessibility.
    """
    print("\n--- Recipes ---")
    for item, ingredients in seed_data.RECIPES.items():
        print(f"Item: {item} | Ingredients: {ingredients}")

    print("\n--- Inventory ---")
    for ing in seed_data.INVENTORY:
        print(f"Name: {ing['name']} | Qty: {ing['quantity']}g | Expiry: {ing['expiry_date']}")

    print("\n--- Orders ---")
    for order in seed_data.ORDERS:
        print(f"Order ID: {order['id']} | Item: {order['item']} | Qty: {order['quantity']}")

    print("\n--- Restock Log ---")
    for record in seed_data.RESTOCK:
        print(f"Ingredient: {record['ingredient']} | Amount: {record['amount']}g")

    print("\n--- Delivery Status ---")
    for status in seed_data.STATUS:
        print(f"Order ID: {status['order_id']} | Delivered: {status['delivered']}")

if __name__ == "__main__":
    try:
        display_data_structures()
        print("\nTask 3: Data inspection complete.")
    except Exception as e:
        print(f"Task 3 Error: {e}")