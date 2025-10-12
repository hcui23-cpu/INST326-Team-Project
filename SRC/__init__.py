"""
Financial Management Function Library

A comprehensive function library for money tracking, categorization, 
and transaction cleaning.

Author: Nathan Urbaez and Haorui Cui
Course: Object-Oriented Programming for Information Science
Institution: University of Maryland, College Park
"""

# Import all functions from the main module
from .library_financial_functions import (
    # Financial Calculations
    calculate_total_spending,
    calculate_average_spending,
    
    # Categorization & Parsing
    categorize_transaction,
    parse_search_query,
    
    # Keyword & Text Analysis
    extract_keywords,
    clean_text_content,
    
    # Validation & Formatting
    validate_url_format,
    format_search_results
)

