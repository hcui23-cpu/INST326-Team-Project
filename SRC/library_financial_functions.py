"""
Finance Tracking Function Library

This module provides utility functions for transaction management including spending calculations, where money is being spent, and trends.

Authors: Nathan Urbaez and Haorui Cui
Course: Object-Oriented Programming for Information Science
"""

# Financial Tracking Functions



# =============================================================================
# Purpose: Formatting and General Purposes
# =============================================================================


def format_currency(amount):
    """Format a number as a currency string using format specifiers."""
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    
    return "${:,.2f}".format(amount)

#-------------------------

import re

def clean_text_content(text):
    """Clean up text by removing numbers, punctuation, and extra spaces.
    
    Prepares text for searching, keyword extraction, or analysis by keeping 
    only letters and spaces, and converting everything to lowercase.
    
    Args:
        text (str): The text to clean.
        
    Returns:
        str: Cleaned lowercase text containing only letters and spaces.
        
    Raises:
        TypeError: If text is not a string.
        
    Examples:
        >>> clean_text_content("Starbucks Coffee #123!")
        'starbucks coffee'
        >>> clean_text_content("Amount: $45.50")
        'amount'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove everything except letters and spaces
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    # Collapse multiple spaces into one and strip edges
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned.lower()

# =============================================================================
# Purpose: Perform financial calculations, data parsing, and categorization.
# =============================================================================

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

#---------

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

#-----------------------------

def categorize_transaction(description):
    """Categorize a financial transaction based on its description.
    
    This function uses keyword matching to assign a transaction
    category (e.g., 'Food', 'Transportation', 'Utilities') based on
    words found in the transaction description. This is to group up 
    spending to know where exactly in what places the money is going.
    
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

#--------------------

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

#--------------------------------

from collections import defaultdict

def analyze_spending_trends(transactions):
    """Analyze spending trends by comparing changes between consecutive months.
    
    This version identifies whether spending patterns show a consistent
    increase, decrease, or volatility over time, rather than just comparing
    averages. It helps users detect behavioral shifts or inconsistent habits.
    
    Args:
        transactions (list[dict]): List of transaction dictionaries.
            Each should contain:
                - 'amount' (float): The transaction amount.
                - 'type' (str): 'expense' or 'income'.
                - 'date' (str): Date in 'YYYY-MM-DD' format.
    
    Returns:
        dict: A dictionary containing:
            - 'monthly_totals': {month: total_spending}
            - 'trend': 'increasing', 'decreasing', 'fluctuating', or 'stable'
            - 'change_rates': List of month-to-month percent changes.
    
    Raises:
        TypeError: If transactions are not valid.
        ValueError: If no valid expenses exist.
    
    Examples:
        >>> data = [
        ...     {"amount": 100.0, "type": "expense", "date": "2024-01-10"},
        ...     {"amount": 120.0, "type": "expense", "date": "2024-02-15"},
        ...     {"amount": 160.0, "type": "expense", "date": "2024-03-12"},
        ...     {"amount": 155.0, "type": "expense", "date": "2024-04-18"},
        ... ]
        >>> analyze_spending_trends(data)
        {'monthly_totals': {'2024-01': 100.0, '2024-02': 120.0, '2024-03': 160.0, '2024-04': 155.0},
         'trend': 'increasing',
         'change_rates': [20.0, 33.33, -3.12]}
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions must be a list of dictionaries")

    monthly_totals = defaultdict(float)

    # Collect monthly totals for expenses
    for t in transactions:
        if not isinstance(t, dict):
            continue
        if t.get("type") != "expense":
            continue
        if "amount" not in t or "date" not in t:
            continue
        try:
            month = t["date"][:7]  # Extract YYYY-MM
            monthly_totals[month] += float(t["amount"])
        except (ValueError, TypeError):
            continue

    if not monthly_totals:
        raise ValueError("No valid expense transactions found.")

    # Sort months and calculate month-to-month change percentages
    months = sorted(monthly_totals.keys())
    totals = [monthly_totals[m] for m in months]

    change_rates = []
    for i in range(1, len(totals)):
        prev, curr = totals[i - 1], totals[i]
        if prev == 0:
            continue
        change = ((curr - prev) / prev) * 100
        change_rates.append(round(change, 2))

    # Interpret pattern of changes
    if not change_rates:
        trend = "stable"
    else:
        positives = sum(1 for c in change_rates if c > 2)
        negatives = sum(1 for c in change_rates if c < -2)
        if positives == len(change_rates):
            trend = "increasing"
        elif negatives == len(change_rates):
            trend = "decreasing"
        elif any(abs(c) > 15 for c in change_rates):
            trend = "fluctuating"
        else:
            trend = "stable"

    return {
        "monthly_totals": dict(monthly_totals),
        "trend": trend,
        "change_rates": change_rates
    }

#-----------------------

def search_transactions(transactions, query):
    """Search for transactions matching a specific keyword or phrase.
    
    This function performs a case-insensitive search through a list
    of transactions and returns those whose descriptions contain
    the search query. This helps users find their exact transactions to 
    keep track of spending.
    
    Args:
        transactions (list[dict]): A list of transaction dictionaries.
            Each dictionary should contain:
                - 'description' (str): The transaction description.
                - 'amount' (float): The transaction amount.
                - 'type' (str): 'expense' or 'income'.
        query (str): The keyword or phrase to search for.
        
    Returns:
        list[dict]: A list of transactions that match the query.
        
    Raises:
        TypeError: If inputs are not valid.
        
    Examples:
        >>> data = [
        ...     {"description": "Target Store Purchase", "amount": 45.75, "type": "expense"},
        ...     {"description": "Walmart Grocery", "amount": 32.00, "type": "expense"},
        ...     {"description": "Payroll Deposit", "amount": 1500.00, "type": "income"}
        ... ]
        >>> search_transactions(data, "walmart")
        [{'description': 'Walmart Grocery', 'amount': 32.0, 'type': 'expense'}]
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions must be a list of dictionaries")
    if not isinstance(query, str):
        raise TypeError("query must be a string")
    
    query_lower = query.lower()
    results = []
    
    for t in transactions:
        if not isinstance(t, dict) or "description" not in t:
            continue
        if query_lower in t["description"].lower():
            results.append(t)
    
    return results

#-----------------------

from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import List, Dict, Any, Optional, Tuple

def is_expense(transaction: dict) -> bool:
    """
    Return True if the transaction dict represents an expense.

    Args:
        transaction (dict): A transaction dictionary with key 'type'.

    Returns:
        bool: True if transaction['type'] is 'expense', False otherwise.

    Examples:
        >>> is_expense({'type': 'expense', 'amount': 12})
        True
        >>> is_expense({'type': 'income', 'amount': 100})
        False
    """
    return isinstance(transaction, dict) and transaction.get("type") == "expense"

#-----------------------

def parse_date(date_str: str) -> str:
    """
    Parse a variety of common date strings and normalize to 'YYYY-MM-DD'.

    Accepts formats such as 'YYYY-MM-DD', 'YYYY/MM/DD', 'MM/DD/YYYY',
    'DD/MM/YYYY', and 'Month DD, YYYY'.

    Args:
        date_str (str): Input date text.

    Returns:
        str: Normalized ISO date string 'YYYY-MM-DD'.

    Raises:
        TypeError: If date_str is not a string.
        ValueError: If the date cannot be parsed.

    Examples:
        >>> parse_date("2024-03-05")
        '2024-03-05'
        >>> parse_date("03/05/2024")
        '2024-03-05'
        >>> parse_date("March 5, 2024")
        '2024-03-05'
    """
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string")

    date_str = date_str.strip()
    fmts = [
        "%Y-%m-%d", "%Y/%m/%d",
        "%m/%d/%Y", "%d/%m/%Y",
        "%b %d, %Y", "%B %d, %Y"
    ]
    for fmt in fmts:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {date_str!r}")

#-----------------------

def filter_transactions_by_date(
    transactions: List[dict],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> List[dict]:
    """
    Return transactions within the inclusive date range [start_date, end_date].

    Args:
        transactions (list[dict]): Each dict has at least 'date' in a parseable format.
        start_date (str|None): Inclusive start date; None to skip lower bound.
        end_date (str|None): Inclusive end date; None to skip upper bound.

    Returns:
        list[dict]: Filtered transactions.

    Raises:
        TypeError: If transactions is not a list.

    Examples:
        >>> data = [{'date': '2024-01-10'}, {'date': '2024-02-05'}]
        >>> [t['date'] for t in filter_transactions_by_date(data, '2024-02-01', '2024-02-28')]
        ['2024-02-05']
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions must be a list of dictionaries")
    
    start = datetime.strptime(parse_date(start_date), "%Y-%m-%d") if start_date else None
    end = datetime.strptime(parse_date(end_date), "%Y-%m-%d") if end_date else None

    out = []
    for t in transactions:
        if not isinstance(t, dict) or "date" not in t:
            continue
        try:
            d = datetime.strptime(parse_date(str(t["date"])), "%Y-%m-%d")
        except Exception:
            continue
        if (start is None or d >= start) and (end is None or d <= end):
            out.append(t)
    return out

#-----------------------

def compute_category_totals(transactions: List[dict]) -> Dict[str, float]:
    """
    Sum expenses by category using your categorize_transaction() helper.

    Args:
        transactions (list[dict]): Dicts with 'type', 'amount', and 'description'.

    Returns:
        dict: {category: total_spent} rounded to 2 decimals.

    Examples:
        >>> tx = [
        ... {'type':'expense','amount':8,'description':'Starbucks'},
        ... {'type':'expense','amount':12,'description':'Uber ride'},
        ... ]
        >>> compute_category_totals(tx)['Food'] > 0
        True
    """
    totals: Dict[str, float] = defaultdict(float)
    for t in transactions:
        if not is_expense(t):
            continue
        try:
            amt = float(t.get("amount", 0))
            cat = categorize_transaction(str(t.get("description", "")))
            totals[cat] += amt
        except Exception:
            continue
    return {k: round(v, 2) for k, v in totals.items()}

#-----------------------

def budget_summary(
    transactions: List[dict],
    category_budgets: Dict[str, float],
    warning_threshold: float = 0.9
) -> Dict[str, Dict[str, float]]:
    """
    Compare category spending against budgets.

    Args:
    transactions (list[dict]): Expense transactions.
    category_budgets (dict): {category: monthly_budget_amount}
    warning_threshold (float): Fraction of budget that triggers 'approaching'.

    Returns:
        dict: {
            category: {
                'spent': float,
                'budget': float,
                'percent_used': float, # 0-100
                'status': 'under'|'approaching'|'exceeded'
            }, ...
        }

    Examples:
        >>> tx = [{'type':'expense','amount':45,'description':'groceries'}]
        >>> budget_summary(tx, {'Food': 100})['Food']['status']
        'under'
    """
    spent = compute_category_totals(transactions)
    result: Dict[str, Dict[str, float]] = {}
    for cat, budget in category_budgets.items():
        s = float(spent.get(cat, 0.0))
        pct = (s / budget * 100.0) if budget > 0 else 0.0
        if budget > 0 and s > budget:
            status = "exceeded"
        elif budget > 0 and s >= warning_threshold * budget:
            status = "approaching"
        else:
            status = "under"
        result[cat] = {
            "spent": round(s, 2),
            "budget": float(budget),
            "percent_used": round(pct, 2),
            "status": status,
        }
    return result

#-----------------------

def top_categories(
    transactions: List[dict], n: int = 3
) -> List[Tuple[str, float]]:
    """
    Return the top-N spending categories by total amount.
    
    Args:
        transactions (list[dict]): List of expense transactions.
        n (int): Number of categories to return.

    Returns:
        list[(category, total)]: Sorted descending by total.

    Examples:
        >>> tx = [
        ... {'type': 'expense', 'amount': 10, 'description': 'coffee'},
        ... {'type': 'expense', 'amount': 30, 'description': 'uber'},
        ... {'type': 'expense', 'amount': 20, 'description': 'lunch'},
        ... ]
        >>> top_categories(tx, 2)[0][1] >= top_categories(tx, 2)[1][1]
        True
    """
    totals = compute_category_totals(transactions)
    return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[: max(0, n)]

#-----------------------

def detect_recurring_expenses(
    transactions: List[dict],
    min_occurrences: int = 3,
    tolerance_days: int = 4
) -> List[dict]:
    """
    Detect recurring expenses (e.g., subscriptions, rent) by merchant and cadence.

    Strategy:
        1) Normalize merchant from description using clean_text_content().
        2) Group expenses by merchant; collect (date, amount).
        3) For each merchant, compute sorted inter-payment gaps in days.
        4) If there is a dominant cadence (e.g., ~30 days) with at least
           `min_occurrences` payments, mark as recurring.
        5) Compute average amount, estimated cadence (median gap), and
           next expected date.

    Args:
        transactions (list[dict]): Dicts with 'type', 'amount', 'description', 'date'.
        min_occurrences (int): Minimum number of payments to treat as recurring.
        tolerance_days (int): Allowed deviation when judging equal cadence.

    Returns:
        list[dict]: Each item like:
            {
                'merchant': str,
                'count': int,
                'average_amount': float,
                'cadence_days': int,
                'last_date': 'YYYY-MM-DD',
                'next_expected_date': 'YYYY-MM-DD'
            }

    Raises:
        TypeError: If transactions is not a list.

    Examples:
        >>> tx = [
        ... {'type':'expense','amount':9.99,'description':'Netflix','date':'2024-01-10'},
        ... {'type':'expense','amount':9.99,'description':'Netflix','date':'2024-02-09'},
        ... {'type':'expense','amount':9.99,'description':'Netflix','date':'2024-03-10'},
        ... ]
        >>> out = detect_recurring_expenses(tx, min_occurrences=3)
        >>> out[0]['merchant'].startswith('netflix')
        True
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions must be a list of dictionaries")

    # 1) Gather expense events by normalized merchant
    series: Dict[str, List[Tuple[datetime, float]]] = defaultdict(list)
    for t in transactions:
        try:
            if not is_expense(t):
                continue
            desc = clean_text_content(str(t.get("description", "")))
            if not desc:
                continue
            d = datetime.strptime(parse_date(str(t.get("date"))), "%Y-%m-%d")
            amt = float(t.get("amount", 0))
            if amt <= 0:
                continue
            series[desc].append((d, amt))
        except Exception:
            continue

    findings: List[dict] = []

    for merchant, events in series.items():
        if len(events) < min_occurrences:
            continue
        events.sort(key=lambda x: x[0])

        # 2) Inter-payment gaps in days
        gaps = [
            (events[i][0] - events[i - 1][0]).days
            for i in range(1, len(events))
        ]
        if not gaps:
            continue

        # 3) Identify dominant cadence (cluster by tolerance)
        counts: Dict[int, int] = defaultdict(int)
        for g in gaps:
            # Snap gap to nearest representative within tolerance
            snapped = None
            for k in list(counts.keys()):
                if abs(g - k) <= tolerance_days:
                    snapped = k
                    break
            if snapped is None:
                counts[g] += 1
            else:
                counts[snapped] += 1

        cadence, freq = max(counts.items(), key=lambda kv: kv[1])
        if freq + 1 < min_occurrences: # +1 because gaps = count-1
            continue

        # 4) Compute stats
        amounts = [amt for _, amt in events]
        avg_amount = sum(amounts) / len(amounts)
        last_date = events[-1][0]
        next_expected = last_date + timedelta(days=cadence)

        findings.append({
            "merchant": merchant,
            "count": len(events),
            "average_amount": round(avg_amount, 2),
            "cadence_days": int(cadence),
            "last_date": last_date.strftime("%Y-%m-%d"),
            "next_expected_date": next_expected.strftime("%Y-%m-%d"),
        })

    # Sort most confident first: more occurrences, then larger amount
    findings.sort(key=lambda d: (d["count"], d["average_amount"]), reverse=True)
    return findings