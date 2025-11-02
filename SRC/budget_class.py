from library_financial_functions import categorize_transaction, format_currency

class Budget:
    def __init__(self, category, limit_amount):
        if limit_amount < 0:
            raise ValueError("Budget limit must be non-negative")
        if not category.strip():
            raise ValueError("Category name cannot be empty")

        self._category = category.strip()
        self._limit = limit_amount
        self._transactions = []
        self._spent = 0.0

    @property
    def category(self):
        return self._category

    @property
    def limit(self):
        return self._limit

    @property
    def spent(self):
        return self._spent

    def add_transaction(self, description, amount):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        category_guess = categorize_transaction(description)
        if category_guess.lower() == self._category.lower():
            self._transactions.append((description, amount))
            self._spent += amount
            return True
        return False

    def remaining(self):
        return max(0, self._limit - self._spent)

    def is_over_budget(self):
        return self._spent > self._limit

    def __str__(self):
        summary = (
            f"Category: {self._category}\n"
            f"Limit: {format_currency(self._limit)}\n"
            f"Spent: {format_currency(self._spent)}\n"
            f"Remaining: {format_currency(self.remaining())}\n"
        )
        if self.is_over_budget():
            summary += "Warning: Over budget!\n"
        if self._transactions:
            summary += "\nTransactions:\n"
            for desc, amt in self._transactions:
                summary += f"- {desc}: {format_currency(amt)}\n"
        else:
            summary += "\nNo transactions recorded yet.\n"
        return summary

