# Financial Management System - Function Library

**Team:** Nathan Urbaez and Haorui Cui
**Domain:** Finance Management
**Course:** INST326 - Object-Oriented Programming for Information Science 

## Project Overview

This function library provides uses for spending query, financial grouping, calculating averages, and viewing trends.

## Problem Statement
Users often struggle with
- Keeping track of their spending
- Searching for financial records
- Detecting spending trends

## Installation and Set Up

1. Clone this repository:


2. No external dependencies required - uses Python standard library only

3. Import functions in your Python code:

from src.library_financial_functions import calculate_total_spending, categorize_transaction

## Quick Usage Examples

```python
from src.library_financial_functions import calculate_total_spending, categorize_transaction, calculate_average_spending

transactions = [
    {"amount": 20.0, "type": "expense", "description": "Burger King lunch"},
    {"amount": 15.5, "type": "expense", "description": "Safeway groceries"},
    {"amount": 100.0, "type": "income", "description": "Payroll deposit"}
]

# Calculate total spending
total = calculate_total_spending(transactions)
print(f"Total spending: ${total}")  # Total spending: $35.5

# Categorize a transaction
category = categorize_transaction(transactions[0]['description'])
print(f"Category: {category}")  # Category: Food

# Calculate average spending for expenses
avg = calculate_average_spending([t['amount'] for t in transactions if t['type'] == 'expense'])
print(f"Average spending: ${avg}")  # Average spending: $17.75
```










