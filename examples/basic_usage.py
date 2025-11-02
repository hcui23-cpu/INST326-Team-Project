# Transcation Example 

from library_financial_functions import parse_date, categorize_transaction, format_currency
from your_budget_module import Budget
from your_transaction_module import Transaction

# Step 1: Pull Transactions
t1 = Transaction("T001", "Target", 45.20, "expense", "2025-11-01")
t2 = Transaction("T002", "Payroll", 2500.00, "income", "2025-11-01")
t3 = Transaction("T003", "FanDuel", 5.50, "expense", "2025-11-02")
t4 = Transaction("T004", "DraftKings", 12000000.00, "expense", "2025-11-01")

transactions = [t1, t2, t3, t4]

# Step 2: Set Budget
food_budget = Budget("Groceries", 200.00)

# Step 3: Import Transactions
for txn in transactions:
    added = food_budget.add_transaction(txn._description, txn.amount)
    if added:
        print(f"Added to budget: {txn}")

# Step 4: Summary
print("\n=== Budget Summary ===")
print(food_budget)

# Step 5: List Transactions
print("\n=== All Transactions ===")
for txn in transactions:
    print(txn.formatted())

