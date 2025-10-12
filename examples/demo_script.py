# demo_script.py
from src.library_financial_functions import (
    calculate_total_spending,
    calculate_average_spending,
    categorize_transaction,
    search_transactions,
    extract_financial_keywords,
    analyze_spending_trends
)

# Sample transactions
transactions = [
    {"amount": 20.0, "type": "expense", "description": "Burger King lunch"},
    {"amount": 15.5, "type": "expense", "description": "Safeway groceries"},
    {"amount": 100.0, "type": "income", "description": "Payroll deposit"},
    {"amount": 45.0, "type": "expense", "description": "Target shopping"}
]

print("=== Financial Management Demo ===\n")

# Total spending
total = calculate_total_spending(transactions)
print(f"Total spending: ${total}")

# Average spending
avg = calculate_average_spending([t['amount'] for t in transactions if t['type'] == 'expense'])
print(f"Average spending: ${avg}")

# Categorize transactions
for t in transactions:
    category = categorize_transaction(t['description'])
    print(f"'{t['description']}' -> Category: {category}")

# Search for a specific merchant
search_results = search_transactions(transactions, "Target")
print("\nSearch Results for 'Target':")
print(search_results)

# Extract keywords from a transaction
keywords = extract_financial_keywords(transactions[1]['description'])
print("\nKeywords from transaction description:")
print(keywords)

# Analyze spending trends
monthly_data = [
    {"amount": 100.0, "type": "expense", "date": "2024-01-10"},
    {"amount": 120.0, "type": "expense", "date": "2024-02-15"},
    {"amount": 90.0, "type": "expense", "date": "2024-03-12"}
]

trends = analyze_spending_trends(monthly_data)
print("\nSpending Trends Analysis:")
print(trends)

