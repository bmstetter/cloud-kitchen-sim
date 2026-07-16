AI Development Usage Log

Date

Task

AI Interaction/Prompt

My Review/Decision

2026-07-15

Setup

Troubleshooting Git 403 access error.

Researched and configured SSH keys instead of HTTPS.

2026-07-16

Tasks 4-5

"Implement Task 4: Recipe Lookup. Keep code simple."

Rejected initial assumption that inventory was a dictionary; forced AI to use the provided list-of-dicts structure from seed data.

2026-07-16

Task 6-7

"Implement Task 6: Fulfillment Logic. Ensure deduction is cumulative."

AI initially reset inventory; I caught this in testing and required a loop to maintain persistent state across multiple orders.

2026-07-16

Task 8

"Implement Task 8: Business Day Manager."

Added a print-out of failure reasons to ensure the requirements for Task 6 and 7 were met for failed orders.

2026-07-16

Task 10

"Implement restock logic with a 1,000g threshold."

Added logic to handle expiry dates; verified the 5-day window requirement against the provided date strings.

2026-07-16

Refactoring

"Review code for clarity and add docstrings."

Accepted docstrings, but manually updated variable names to be more descriptive.

2026-07-16

Final Test

"Generate test suite for all tasks."

AI provided tests; I manually synced the test logic with the actual function signatures to fix import errors.