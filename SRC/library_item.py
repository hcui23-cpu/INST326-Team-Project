from __future__ import annotations

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field

# Import the functional library (assumed to be in same SRC package/dir)
from library_financial_functions import (
    format_currency,
    clean_text_content,
    calculate_total_spending,
    categorize_transaction,
    extract_financial_keywords,
    analyze_spending_trends,
    search_transactions,
    is_expense,
    parse_date,
    filter_transactions_by_date,
    compute_category_totals,
    budget_summary,
    top_categories as _top_categories_fn,  # in case available
    detect_recurring_expenses,
)


@dataclass
class Transaction:
    """Lightweight transaction record used by FinanceLedger.

    Attributes:
        ttype: 'expense' or 'income'
        amount: Positive numeric amount (float)
        description: Free-text description (merchant, note, etc.)
        date: Normalized 'YYYY-MM-DD' date string
    """
    ttype: str
    amount: float
    description: str
    date: str

    def __post_init__(self) -> None:
        # Validate type
        if self.ttype not in {'expense', 'income'}:
            raise ValueError("ttype must be either 'expense' or 'income'")
        # Validate amount
        try:
            self.amount = float(self.amount)
        except Exception as exc:
            raise TypeError("amount must be numeric") from exc
        if self.amount < 0:
            raise ValueError("amount must be non-negative")
        # Normalize/validate date
        self.date = parse_date(self.date)
        # Ensure description is a string
        if not isinstance(self.description, str):
            raise TypeError("description must be a string")


class FinanceLedger:
    """Manage a collection of financial transactions for a single user.

    Parameters
    ----------
    owner : str
        Name/identifier for the owner of this ledger.
    category_budgets : Optional[Dict[str, float]]
        Optional mapping of category -> monthly budget amount.

    Examples
    --------
    >>> ledger = FinanceLedger('Alex', {'food': 200.0, 'entertainment': 80.0})
    >>> ledger.add_transaction('Coffee at Starbucks', 4.75, '2024-10-05', 'expense')
    >>> ledger.add_transaction('Paycheck', 1200, '2024-10-07', 'income')
    >>> round(ledger.total_spent(), 2)
    4.75
    >>> any('coffee' in t['description'].lower() for t in ledger.search('coffee'))
    True
    """

    # ----------------------- Initialization & Encapsulation -----------------------
    def __init__(self, owner: str, category_budgets: Optional[Dict[str, float]] = None) -> None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("owner must be a non-empty string")
        if category_budgets is not None and not isinstance(category_budgets, dict):
            raise TypeError("category_budgets must be a dict or None")
        # Store private attributes
        self._owner: str = owner.strip()
        self._transactions: List[Dict] = []  # list of dicts (compatible with Project 1 functions)
        self._category_budgets: Dict[str, float] = {k.lower(): float(v) for k, v in (category_budgets or {}).items()}

    # Properties for controlled access
    @property
    def owner(self) -> str:
        """Read-only owner name."""
        return self._owner

    @property
    def transactions(self) -> List[Dict]:
        """A COPY of transactions to preserve encapsulation."""
        return list(self._transactions)

    @property
    def category_budgets(self) -> Dict[str, float]:
        """A COPY of category budgets (category -> monthly budget)."""
        return dict(self._category_budgets)

    # ----------------------- Core Behaviors (Integrate P1 Functions) ---------------
    def add_transaction(self, description: str, amount: float, date: str, ttype: str = 'expense') -> Transaction:
        """Add a validated transaction to the ledger.

        Integrates: parse_date() & categorize_transaction() through normalization.

        Returns
        -------
        Transaction
            The created Transaction dataclass instance.
        """
        tx = Transaction(ttype=ttype, amount=amount, description=description, date=date)
        # Store as a dict that matches Project 1 expected schema
        record = {'type': tx.ttype, 'amount': tx.amount, 'description': tx.description, 'date': tx.date}
        self._transactions.append(record)
        return tx

    def total_spent(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> float:
        """Compute total expenses in an optional date range.

        Integrates: filter_transactions_by_date() + calculate_total_spending().
        """
        data = self._transactions
        if start_date or end_date:
            data = filter_transactions_by_date(data, start_date, end_date)
        return calculate_total_spending(data)

    def month_summary(self, year: int, month: int) -> Dict[str, Dict[str, float]]:
        """Return a budget and category summary for the given month.

        Integrates: filter_transactions_by_date(), compute_category_totals(), budget_summary().

        Returns
        -------
        dict
            {
              'totals': {category: total_spent, ...},
              'budget_status': {category: {'spent': x, 'budget': y, 'percent_used': z, 'status': 'under'|'approaching'|'exceeded'}},
            }
        """
        if not (1 <= int(month) <= 12):
            raise ValueError("month must be in 1..12")
        start = f"{int(year):04d}-{int(month):02d}-01"
        # simple month end: filter function treats end as inclusive; choose a large day and rely on parsing
        end = f"{int(year):04d}-{int(month):02d}-31"
        month_tx = filter_transactions_by_date(self._transactions, start, end)
        totals = compute_category_totals(month_tx)
        budget_status = budget_summary(month_tx, self._category_budgets) if self._category_budgets else {}
        return {'totals': totals, 'budget_status': budget_status}

    def search(self, query: str) -> List[Dict]:
        """Search transactions by keyword (case-insensitive).

        Integrates: search_transactions().
        """
        return search_transactions(self._transactions, query)

    def top_categories(self, n: int = 3) -> List[Tuple[str, float]]:
        """Return top-n categories by total expense amount.

        Integrates: compute_category_totals().
        """
        totals = compute_category_totals(self._transactions)
        return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:max(0, int(n))]

    def detect_recurring(self, min_occurrences: int = 3, tolerance_days: int = 4) -> List[Dict]:
        """Detect recurring expenses (e.g., subscriptions) with cadence.

        Integrates: detect_recurring_expenses().
        """
        return detect_recurring_expenses(self._transactions, min_occurrences=min_occurrences, tolerance_days=tolerance_days)

    def trend(self) -> Dict:
        """Analyze spending trend across months.

        Integrates: analyze_spending_trends().
        """
        return analyze_spending_trends(self._transactions)

    # ----------------------- Representations ---------------------------------------
    def __str__(self) -> str:
        total = 0.0
        try:
            total = calculate_total_spending(self._transactions)
        except Exception:
            total = 0.0
        return f"FinanceLedger(owner={self._owner}, expenses={format_currency(total)})"

    def __repr__(self) -> str:
        return f"FinanceLedger(owner={self._owner!r}, transactions={len(self._transactions)}, budgets={list(self._category_budgets.keys())})"
