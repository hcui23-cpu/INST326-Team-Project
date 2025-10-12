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

# Financial Calculations

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
print(f"Average spending: ${avg}")  # Average spending: $17.38
```

# Searching Transactions

```python
from src.library_financial_functions import search_transactions

# Search for transactions containing "Olive Garden"
results = search_transactions(transactions, "Olive Garden")
print(results)
# [{'amount': 15.5, 'type': 'expense', 'description': 'Olive Garden restraunt'}]
```

# Extracting Keywords

```python
from src.library_financial_functions import search_transactions

# Search for transactions containing "safeway"
results = search_transactions(transactions, "safeway")
print(results)
# [{'amount': 15.5, 'type': 'expense', 'description': 'Safeway groceries'}]
```

## Function Library Overview

Our library contains 15 specialized functions organized into categories:

### Categorizing and Formatting
- `format_currency` - Format numbers into dollars ($17.38)
- `clean_text_content()` - Get rid of extra symbols, spaces, or numbers. Lowercase text for searching

### Financial Calculations
- `calculate_total_spending()` - Get a sum of all spending
- `calculate_average_spending()` - Compute the average spending amount
- `categorize_transaction()` - Use keywords to group transactions

### Transaction Analysis
- `extract_financial_keywords()` - Pull common keywords from transactions
- `analyze_spending_trends()` - View spending trends
- `search_transactions()` - Search for specific transactions

## Team Member Contributions

**Nathan Urbaez** - Financial Analysis and Calculations
- Implemented 2 formatting functions
- Implemented 6 financial transaction and calculation functions

**Haorui Cui**




## AI Collaboration Documentation

Team members used AI assistance for:
- Initial Function Generation
- Function formatting and debugging
- Github Formatting

All AI-generated code was thoroughly reviewed, tested, and modified to meet project requirements. Individual AI collaboration details documented in personal repositories.

---

## Repository Structure

---

INST326-Team-Project/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── library_financial_functions.py
│   └── utils.py
├── docs/
│   ├── function_reference.md
│   └── usage_examples.md
├── examples/
│   └── demo_script.py
└── requirements.txt








