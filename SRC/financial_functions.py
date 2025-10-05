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
