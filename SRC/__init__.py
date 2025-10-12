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

# Define what gets imported with "src.library_financial_funcations *"
__all__ = [
    # Formatting and General Utilities
    'format_currency',
    'clean_text_content',
    
    # Financial Calculations and Categorization
    'calculate_average_spending',
    'calculate_total_spending',
    'categorize_transaction',
    
    # Financial Data Analysis
    'extract_financial_keywords',
    'analyze_spending_trends',
    'search_transactions'
]

# Convenience function groupings for easier access
# Formatting and General Utilities
UTILITY_FUNCTIONS = [
    'format_currency',
    'clean_text_content'
]

# Financial Calculations and Categorization
FINANCIAL_FUNCTIONS = [
    'calculate_average_spending',
    'calculate_total_spending',
    'categorize_transaction'
]

# Financial Data Analysis and Retrieval
ANALYSIS_FUNCTIONS = [
    'extract_financial_keywords',
    'analyze_spending_trends',
    'search_transactions'
]

def get_function_categories():
    """Get a dictionary of function categories and their associated functions.
    
    Returns:
        dict[str, list[str]]: Dictionary mapping category names to function lists.
        
    Example:
        >>> categories = get_function_categories()
        >>> print(categories['financial'])
        ['calculate_average_spending', 'calculate_total_spending', 'categorize_transaction']
    """
    return {
        'utility': UTILITY_FUNCTIONS,
        'financial': FINANCIAL_FUNCTIONS,
        'analysis': ANALYSIS_FUNCTIONS
    }


def list_all_functions():
    """List all available functions in the finance library.
    
    Returns:
        list[str]: Alphabetically sorted list of all function names.
        
    Example:
        >>> functions = list_all_functions()
        >>> print(f"Total functions: {len(functions)}")
        Total functions: 8
    """
    return sorted(__all__)


def get_library_info():
    """Get finance library metadata and information.
    
    Returns:
        dict[str, str]: Dictionary containing library information.
        
    Example:
        >>> info = get_library_info()
        >>> print(f"Version: {info['version']}")
        Version: 1.0.0
    """
    return {
        'name': 'Financial Management Function Library',
        'version': __version__,
        'author': __author__,
        'description': __description__,
        'total_functions': len(__all__),
        'categories': list(get_function_categories().keys()),
        'license': __license__
    }

# Quick usage example for interactive help
def quick_start():
    """Display quick start information for new users.
    
    Example:
        >>> import finance_library
        >>> finance_library.quick_start()
    """
    print("Finance Management Function Library - Quick Start")
    print("=" * 50)
    print()
    print("This library provides 15 functions for financial tracking")
    print()
    
    categories = get_function_categories()
    for category, functions in categories.items():
        print(f"📋 {category.title()} Functions ({len(functions)}):")
        for func in functions:
            print(f"   • {func}")
        print()
    
    print("💡 Quick Examples:")
    print("   # Calculate total spending")
    print("   >>> total = calculate_total_spending(transactions)")
    print("   >>> print(f'Total Spending: ${total:.2f}')")
    print()
    print("   # Average spending by category")
    print("   >>> avg = calculate_average_spending(transactions, category='Food')")
    print("   >>> print(f'Average Food Spending: ${avg:.2f}')")
    print()
    print("   # Format and display search results")
    print("   >>> results = format_search_results(search_transactions('walmart'))")
    print("   >>> for r in results: print(r)")
    print()
    print("📚 For detailed documentation, see docs/function_reference.md")
    print("🎯 For examples, run examples/demo_script.py")


if __name__ == "__main__":
    # If someone runs "python -m finance_library", show quick start
    quick_start()
