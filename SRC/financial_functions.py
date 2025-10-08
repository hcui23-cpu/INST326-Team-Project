"""
Finance Tracking Function Library

This module provides utility functions for transaction management including spending calculations, where money is being spent, and trends.

Authors: Nathan Urbaez and Haorui Cui
Course: Object-Oriented Programming for Information Science
"""

# Financial Tracking Functions

def extract_financial_keywords(description, top_k=5):
    """Extract the most relevant financial keywords from a transaction description.
    
    This version uses smarter filtering for financial contexts by excluding 
    generic terms and emphasizing words that are meaningful for categorizing
    spending (e.g., brand names, merchants, and purchase types).
    
    Args:
        description (str): The transaction text (e.g., "Starbucks Coffee Shop Purchase").
        top_k (int): Number of keywords to return (default is 5).
        
    Returns:
        list[str]: A list of the top extracted keywords in lowercase order of importance.
        
    Raises:
        TypeError: If description is not a string or top_k is not an integer.
        
    Examples:
        >>> extract_financial_keywords("Amazon Prime Video Subscription - Entertainment", 4)
        ['amazon', 'prime', 'video', 'entertainment']
    """
    if not isinstance(description, str):
        raise TypeError("description must be a string")
    if not isinstance(top_k, int) or top_k <= 0:
        raise TypeError("top_k must be a positive integer")
    
    # Convert to lowercase and tokenize words
    tokens = re.findall(r"[a-zA-Z]+", description.lower())
    
    # Expanded stopword list for finance data
    stopwords = {
        "the", "and", "for", "of", "to", "a", "in", "on", "at",
        "payment", "purchase", "transaction", "from", "with", "store"
    }
    
    # Keep only meaningful tokens
    filtered_tokens = [t for t in tokens if t not in stopwords and len(t) > 2]
    
    if not filtered_tokens:
        return []
    
    # Count frequency of each token
    counts = Counter(filtered_tokens)
    
    # Rank and return top_k keywords
    keywords = [word for word, _ in counts.most_common(top_k)]
    return keywords

#----------------------------------------

def calculate_average_spending(transactions):
    """Calculate the average spending amount from a list of transactions.
    
    This function computes the mean spending value from a list of numeric transaction
    amounts (e.g., debit transactions, purchases). It ignores invalid or non-numeric
    entries and raises errors for empty or invalid input.
    
    Args:
        transactions (list[float | int]): A list of transaction amounts.
        
    Returns:
        float: The average (mean) spending value, rounded to two decimal places.
        
    Raises:
        TypeError: If transactions is not a list or contains non-numeric values.
        ValueError: If the list is empty or contains no valid spending data.
        
    Examples:
        >>> calculate_average_spending([25.50, 40.00, 10.75, 23.25])
        24.88
        >>> calculate_average_spending([])
        Traceback (most recent call last):
            ...
        ValueError: Transaction list is empty or contains no valid spending data.
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions must be provided as a list of numbers")
    
    valid_amounts = [float(t) for t in transactions if isinstance(t, (int, float))]
    
    if not valid_amounts:
        raise ValueError("Transaction list is empty or contains no valid spending data.")
    
    avg_spending = sum(valid_amounts) / len(valid_amounts)
    return round(avg_spending, 2)


#-------------------------------------

def calculate_total_spending(transactions):
    """Calculate the total spending from a list of transactions.
    
    This function sums all valid expense amounts from a list of transactions. 
    It ignores income entries or invalid data, helping users quickly determine 
    their total spending over a specific period.
    
    Args:
        transactions (list[dict]): A list of transaction dictionaries. 
            Each dictionary should contain:
            - 'amount' (float): The transaction amount
            - 'type' (str): Either 'expense' or 'income'
            
    Returns:
        float: The total amount spent, rounded to two decimal places.
        
    Raises:
        TypeError: If transactions is not a list or contains invalid entries.
        ValueError: If no valid expense transactions are found.
        
    Examples:
        >>> data = [
        ...     {"amount": 20.0, "type": "expense"},
        ...     {"amount": 15.5, "type": "expense"},
        ...     {"amount": 100.0, "type": "income"}
        ... ]
        >>> calculate_total_spending(data)
        35.5
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions must be provided as a list of dictionaries")
    
    total = 0.0
    for t in transactions:
        if not isinstance(t, dict):
            raise TypeError("Each transaction must be a dictionary")
        if "amount" not in t or "type" not in t:
            raise TypeError("Each transaction must include 'amount' and 'type' keys")
        if t["type"] == "expense" and isinstance(t["amount"], (int, float)):
            total += float(t["amount"])
    
    if total == 0.0:
        raise ValueError("No valid expense transactions found.")
    
    return round(total, 2)

#-------------------------------------------------------------------------------------------

def format_currency(amount):
    """Format a number as a currency string using format specifiers."""
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    
    return "${:,.2f}".format(amount)

#-----------------------------------------------------------------------------------------

def categorize_transaction(description):
    """Categorize a financial transaction based on its description.
    
    This function uses keyword matching to assign a transaction
    category (e.g., 'Food', 'Transportation', 'Utilities') based on
    words found in the transaction description. It helps automate
    financial data labeling for spending reports and retrieval tasks.
    
    Args:
        description (str): The transaction description 
            (e.g., "Marathon Deli Lunch Purchase").
            
    Returns:
        str: The detected spending category (default: "Other").
        
    Raises:
        TypeError: If description is not a string.
        
    Examples:
        >>> categorize_transaction("Uber ride to airport")
        'Transportation'
        >>> categorize_transaction("Netflix monthly subscription")
        'Entertainment'
        >>> categorize_transaction("Burger King order")
        'Food'
    """
    if not isinstance(description, str):
        raise TypeError("description must be a string")
    
    desc = description.lower()
    
    categories = {
        "Food": [
            "restaurant", "coffee", "cafe", "burger", "pizza", "bar",
            "starbucks", "mcdonalds", "kfc", "burger king", "safeway",
            "trader joes", "giant", "lidl", "marathon deli"
        ],
        "Transportation": ["uber", "lyft", "taxi", "bus", "train", "flight", "airline", "gas", "fuel"],
        "Utilities": ["electric", "water", "gas bill", "internet", "wifi", "phone", "utility"],
        "Entertainment": [
            "movie", "netflix", "spotify", "game", "cinema", "concert", "music",
            "steam", "fortnite"
        ],
        "Shopping": ["walmart", "target", "amazon", "mall", "store", "purchase"],
        "Income": ["deposit", "salary", "payroll", "transfer from employer", "income"],
        "Health": ["pharmacy", "doctor", "hospital", "clinic", "medication", "dentist"],
        "Travel": ["hotel", "airbnb", "booking", "expedia", "trip", "travel"]
    }
    
    for category, keywords in categories.items():
        if any(word in desc for word in keywords):
            return category
    
    return "Other"


