from finance_functions import calculate_average_spending, analyze_spending_trends

class SpendingAnalyzer:
    def __init__(self, transactions):
        if not isinstance(transactions, list):
            raise ValueError("transactions must be provided as a list.")
        if not all(hasattr(t, "amount") and hasattr(t, "txn_type") for t in transactions):
            raise ValueError("Each transaction must have 'amount' and 'txn_type' attributes.")
        self._transactions = transactions

    @property
    def transactions(self):
        return self._transactions

    def average_spending(self, category=None):
        relevant_txns = [
            t.amount for t in self._transactions
            if t.txn_type == "expense" and (category is None or getattr(t, "category", None) == category)
        ]
        return calculate_average_spending(relevant_txns)

    def spending_trends(self):
        data = [{"amount": t.amount, "date": t.date, "category": getattr(t, "category", "Uncategorized")}
                for t in self._transactions]
        return analyze_spending_trends(data)

    def total_spent(self):
        return sum(t.amount for t in self._transactions if t.txn_type == "expense")

    def top_categories(self, n=3):
        category_totals = {}
        for t in self._transactions:
            if t.txn_type == "expense":
                category = getattr(t, "category", "Uncategorized")
                category_totals[category] = category_totals.get(category, 0) + t.amount
        sorted_totals = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
        return sorted_totals[:n]

    def __str__(self):
        avg = self.average_spending()
        total = self.total_spent()
        return f"Total spent: ${total:,.2f} | Average per transaction: ${avg:,.2f}"

