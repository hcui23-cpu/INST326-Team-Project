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
    {"amount": 20.0, "type": "expense", "description": "Hooters"},
    {"amount": 100.0, "type": "income", "description": "Payroll"}
]
calculate_total_spending(transactions)  # 20.0
```

```calculate_average_spending(transactions)```

```python
calculate_average_spending([20, 15.5, 23])  # 19.5
```

