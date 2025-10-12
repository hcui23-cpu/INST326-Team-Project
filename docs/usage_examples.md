# Examples on Usage

## 1. Preparing the library

```python
# Import the main functions
from src.library_financial_functions import (
    calculate_total_spending,
    calculate_average_spending,
    categorize_transaction,
    search_transactions,
    extract_financial_keywords,
    analyze_spending_trends
)
```
## 2. Calculations

```python
transactions = [
    {"amount": 20.0, "type": "expense", "description": "Burger King lunch"},
    {"amount": 15.5, "type": "expense", "description": "Safeway groceries"},
    {"amount": 100.0, "type": "income", "description": "Payroll deposit"}
]

# Calculate total spending
total = calculate_total_spending(transactions)
print(f"Total spending: ${total}")  # Output: $35.5

# Calculate average spending (expenses only)
avg = calculate_average_spending([t['amount'] for t in transactions if t['type'] == 'expense'])
print(f"Average spending: ${avg}")  # Output: $17.38

# Categorize a transaction
category = categorize_transaction(transactions[0]['description'])
print(f"Category: {category}")  # Output: Food
```

## 3. Searching through transactions

```python
# Search for transactions containing "Safeway"
results = search_transactions(transactions, "Safeway")
print(results)
# Output: [{'amount': 15.5, 'type': 'expense', 'description': 'Safeway groceries'}]
```

## 4. Keyword extraction

```python
# Extract top keywords from a transaction description
keywords = extract_financial_keywords("Amazon Prime Video Subscription", top_k=4)
print(keywords)
# Output: ['amazon', 'prime', 'video', 'subscription']
```

## 5. Analyzing spending trends

```python
monthly_data = [
    {"amount": 100.0, "type": "expense", "date": "2024-01-10"},
    {"amount": 120.0, "type": "expense", "date": "2024-02-15"},
    {"amount": 90.0, "type": "expense", "date": "2024-03-12"}
]

trends = analyze_spending_trends(monthly_data)
print(trends)
# Output:
# {'monthly_totals': {'2024-01': 100.0, '2024-02': 120.0, '2024-03': 90.0},
#  'trend': 'fluctuating',
#  'change_rates': [20.0, -25.0]}
```








