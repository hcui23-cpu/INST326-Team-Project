from library_financial_functions import parse_date, categorize_transaction, format_currency

class Transaction:
    def __init__(self, txn_id, description, amount, txn_type, date):
        if not isinstance(txn_id, str) or not txn_id.strip():
            raise ValueError("Transaction ID must be a non-empty string.")
        if txn_type not in {"expense", "income"}:
            raise ValueError("txn_type must be 'expense' or 'income'.")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number.")
        
        self._txn_id = txn_id
        self._description = description.strip()
        self._amount = float(amount)
        self._txn_type = txn_type
        self._date = parse_date(date)
        self._category = categorize_transaction(description)

    @property
    def txn_id(self):
        return self._txn_id

    @property
    def amount(self):
        return self._amount

    @property
    def txn_type(self):
        return self._txn_type

    @property
    def date(self):
        return self._date

    @property
    def category(self):
        return self._category

    def formatted(self):
        sign = "-" if self._txn_type == "expense" else "+"
        return f"[{self._date}] {self._description} ({self._category}): {sign}{format_currency(self._amount)}"

    def __str__(self):
        return f"{self._txn_id}: {self.formatted()}"

