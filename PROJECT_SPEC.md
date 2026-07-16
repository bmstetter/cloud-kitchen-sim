Project Specification: Cloud Kitchen Simulator

1. Project Purpose

A delivery-only management system to automate recipe lookups, inventory deductions, and restocking for multiple virtual restaurant brands.

2. Core Data Structures (from seed_data.py)

Recipes: Dictionary mapping menu items to ingredient lists.

Inventory: List of dictionaries (name, quantity, expiry_date).

Orders: List of dictionaries (id, item, quantity).

Restock: List of dictionaries (ingredient, amount).

Status: List of dictionaries (order_id, delivered, reason).

3. Business Rules

Cumulative Deduction: Inventory must remain persistent across all order processing.

Low-Stock Threshold: $1,000g$.

Expiry Window: Items expiring within 5 days of current date are flagged.

Par Level: Target restocking amount is $10,000g$.

Fulfillment: All-or-nothing approach; orders fail if any ingredient is missing or insufficient.

4. Implementation Status

[x] Task 1: Project Setup

[x] Task 2: Project Spec Creation

[x] Task 3: Data Loading & Inspection

[x] Task 4: Recipe Lookup

[x] Task 5: Inventory Availability Check

[x] Task 6: Fulfillment Logic

[x] Task 7: Cumulative Order Processing

[x] Task 8: Restock and Expiry Rules

[x] Task 9: Business-Friendly Summary

[x] Task 10: Refactoring & Review

5. Known Assumptions

The simulation assumes the current date for expiry calculation is today (2026-07-16).

Ingredient quantities are stored and processed in grams.

6. Next Steps

Final submission verification.