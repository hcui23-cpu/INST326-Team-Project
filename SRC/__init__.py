"""
Financial Management Function Library

A comprehensive function library for money tracking, categorization, 
and transaction cleaning.

Author: Nathan Urbaez and Haorui Cui
Course: Object-Oriented Programming for Information Science
Institution: University of Maryland, College Park
"""

# Package metadata
__version__ = "1.0.0"
__authors__ = "Nathan Urbaez and Haorui Cui"
__email__ = "nurbaez@terpmail.umd.edu - hcui23@terpmail.umd.edu"
__description__ = "Financial Management Function Library for INST326"

# Import main functions for easy access
from src.library_financial_funcations import (
    # Formatting and Text Cleaning
    format_currency,
    clean_text_content,
    
    # Financial Calculations and Categorization
    calculate_average_spending,
    calculate_total_spending,
    categorize_transaction,
    
    # Information Retrieval and Analysis
    extract_financial_keywords,
    search_transactions,
    analyze_spending_trends
)

