# Example usage for functions


## Categorizing and Formatting

```format_currency(amount)```
```python
format_currency(17.38)  # "$17.38"
```

```clean_text_content(text)```

```python
clean_text_content("WalMart  ")  # "walmart"
```

```categorize_transaction(description)```

```python
categorize_transaction("Burger King lunch")  # "Food"
```

## Financial Calculations

```calculate_total_spending(transactions)```

```python
transactions = [
    {"amount": 20.0, "type": "expense", "description": "Burger King"},
    {"amount": 100.0, "type": "income", "description": "Payroll"}
]
calculate_total_spending(transactions)  # 20.0
```

```calculate_average_spending(transactions)```

```python
calculate_average_spending([20, 15.5, 23])  # 19.5
```

## Transaction Analysis

```extract_financial_keywords(description, top_k=5)```

```
extract_financial_keywords("Amazon Prime Video Subscription", 4)  
# ["amazon", "prime", "video", "subscription"]
```

```analyze_spending_trends(transactions)```

```python
data = [
    {"amount": 100.0, "type": "expense", "date": "2024-01-10"},
    {"amount": 120.0, "type": "expense", "date": "2024-02-15"}
]
analyze_spending_trends(data)
# {"monthly_totals": {"2024-01": 100.0, "2024-02": 120.0}, "trend": "increasing", "change_rates": [20.0]}
```

```search_transactions(transactions, query)```

```python
search_transactions(transactions, "safeway")
# [{"amount": 15.5, "type": "expense", "description": "Safeway groceries"}]
```




