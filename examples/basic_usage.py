# Transaction Example 

from library_financial_functions import parse_date, categorize_transaction, format_currency
from budget_class import Budget
from transaction_module import Transaction

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

# Analyzing Spending Example

from library_financial_functions import calculate_average_spending, analyze_spending_trends
from transaction_class import Transaction
from spending_analyzer import SpendingAnalyzer

# Step 1: Transactions
t1 = Transaction("T001", "Groceries at Safeway", 45.20, "expense", "2025-11-01")
t2 = Transaction("T002", "Salary", 2500.00, "income", "2025-11-01")
t3 = Transaction("T003", "Coffee at Starbucks", 5.50, "expense", "2025-11-02")
t4 = Transaction("T004", "Online Course", 120.00, "expense", "2025-11-01")
t5 = Transaction("T005", "Pizza Hut", 35.75, "expense", "2025-11-03")

transactions = [t1, t2, t3, t4, t5]

# Step 2: Run the analyzer
analyzer = SpendingAnalyzer(transactions)

# Step 3: Calculate Total and Average
print("=== Spending Summary ===")
print(analyzer)  

# Step 4: Seperate into categories
categories = set(t.category for t in transactions if t.txn_type == "expense")
for cat in categories:
    avg = analyzer.average_spending(category=cat)
    print(f"Average spending in {cat}: ${avg:.2f}")

# Step 5: Display top spending
print("\nTop spending categories:")
for cat, amt in analyzer.top_categories(n=3):
    print(f"{cat}: ${amt:.2f}")

# Step 6: Analyze spending habits
print("\nSpending trends data:")
trends = analyzer.spending_trends()
for entry in trends:
    print(entry)
