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

from src.library_financial_functions import calculate_total_spending, calculate_average_spending

# Calculate total spending from all transactions
transactions = [
    {"amount": 45.20, "type": "expense"},
    {"amount": 1200.00, "type": "income"},
    {"amount": 12.50, "type": "expense"}
]
total = calculate_total_spending(transactions)  # 57.70

# Calculate average spending per expense transaction
average = calculate_average_spending(transactions)  # 28.85


from src.library_financial_functions import categorize_transaction, analyze_spending_trends

# Categorize transactions automatically
transactions = [
    {"description": "Burger King", "amount": 12.99},
    {"description": "Steam", "amount": 49.99},
    {"description": "Payroll Deposit", "amount": 1500.00}
]
categorized = [categorize_transaction(t["description"]) for t in transactions]
# ['Food', 'Entertainment', 'Income']

# Analyze monthly spending trends
trend_data = analyze_spending_trends(transactions)
# {'Food': 12.99, 'Entertainment': 49.99, 'Income': 1500.00}

from src.library_financial_functions import clean_text_content, format_search_results

# Clean messy transaction text for keyword extraction
text = clean_text_content("Target Store #3948 - 25.00 USD")
# 'target store usd'

# Format search results neatly
results = [
    {"merchant": "Walmart", "amount": 32.10, "category": "Retail"},
    {"merchant": "Lidl", "amount": 15.40, "category": "Food"}
]
formatted = format_search_results(results)
# "Retail - Walmart: $32.10\nFood - Lidl: $15.40"





