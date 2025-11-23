"""
Comprehensive test suite for Finance System.

Tests inheritance, polymorphism, abstract base classes, and composition.
"""

import unittest
from abc import ABC
from finance_ledger import (
    AbstractTransaction,
    ExpenseTransaction,
    IncomeTransaction,
    FinanceLedger,
)

import unittest
from abc import ABC
from finance_ledger import (
    AbstractTransaction,
    ExpenseTransaction,
    IncomeTransaction,
    FinanceLedger,
)


class TestInheritance(unittest.TestCase):
    """Test inheritance hierarchies."""

    def test_transaction_inheritance(self):
        """ExpenseTransaction and IncomeTransaction inherit from AbstractTransaction."""
        expense = ExpenseTransaction(50.0, "2025-11-01", "Food")
        income = IncomeTransaction(1000.0, "2025-11-05", "Payroll")

        self.assertIsInstance(expense, AbstractTransaction)
        self.assertIsInstance(income, AbstractTransaction)


class TestPolymorphism(unittest.TestCase):
    """Test polymorphic behavior across transaction types."""

    def test_impact_on_balance(self):
        """Different transactions affect balance differently."""
        expense = ExpenseTransaction(50.0, "2025-11-01", "Groceries")
        income = IncomeTransaction(1000.0, "2025-11-05", "Salary")

        self.assertEqual(expense.impact_on_balance(), -50.0)
        self.assertEqual(income.impact_on_balance(), 1000.0)

    def test_ttype_property(self):
        """Different transactions report correct ttype."""
        expense = ExpenseTransaction(25.0, "2025-11-02", "Coffee")
        income = IncomeTransaction(500.0, "2025-11-03", "Bonus")

        self.assertEqual(expense.ttype, "expense")
        self.assertEqual(income.ttype, "income")


class TestAbstractBaseClasses(unittest.TestCase):
    """Test that AbstractTransaction enforces implementation."""

    def test_cannot_instantiate_abstract_transaction(self):
        """AbstractTransaction should not be directly instantiable."""
        with self.assertRaises(TypeError):
            AbstractTransaction(50.0, "2025-11-01", "Test")


class TestComposition(unittest.TestCase):
    """Test FinanceLedger composition of transactions."""

    def setUp(self):
        self.ledger = FinanceLedger("Alex", {"food": 200, "entertainment": 80})

    def test_add_transaction_stores_record(self):
        """Transactions are stored correctly as dicts."""
        tx = self.ledger.add_transaction("expense", "Lunch", 15.0, "2025-11-01")
        self.assertEqual(tx.ttype, "expense")
        self.assertIn("amount", self.ledger.transactions[0])
        self.assertEqual(self.ledger.transactions[0]["description"], "Lunch")

    def test_total_spent_calculation(self):
        """Total spent correctly sums expenses."""
        self.ledger.add_transaction("expense", "Lunch", 15.0, "2025-11-01")
        self.ledger.add_transaction("expense", "Coffee", 5.0, "2025-11-01")
        self.ledger.add_transaction("income", "Salary", 1000.0, "2025-11-01")
        total = self.ledger.total_spent()
        self.assertEqual(total, 20.0)

    def test_search_functionality(self):
        """Ledger search finds matching transactions."""
        self.ledger.add_transaction("expense", "Lunch at Cafe", 12.0, "2025-11-01")
        self.ledger.add_transaction("income", "Salary", 1000.0, "2025-11-01")
        results = self.ledger.search("lunch")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["description"], "Lunch at Cafe")

    def test_month_summary_returns_expected_keys(self):
        """month_summary returns totals and budget_status."""
        self.ledger.add_transaction("expense", "Dinner", 50.0, "2025-11-10")
        summary = self.ledger.month_summary(2025, 11)
        self.assertIn("totals", summary)
        self.assertIn("budget_status", summary)
        self.assertIsInstance(summary["totals"], dict)
        self.assertIsInstance(summary["budget_status"], dict)

    def test_top_categories(self):
        """Top categories returns sorted list of tuples."""
        self.ledger.add_transaction("expense", "Dinner", 50.0, "2025-11-10")
        self.ledger.add_transaction("expense", "Movie", 30.0, "2025-11-11")
        top = self.ledger.top_categories(2)
        self.assertEqual(top[0][0], "dinner")  # category computed in your compute_category_totals
        self.assertEqual(len(top), 2)

    def test_detect_recurring(self):
        """Recurring expenses detection returns a list."""
        for i in range(3):
            self.ledger.add_transaction("expense", "Netflix", 15.0, f"2025-11-0{i+1}")
        recurring = self.ledger.detect_recurring(min_occurrences=3)
        self.assertTrue(isinstance(recurring, list))
        self.assertTrue(len(recurring) > 0)

    def test_trend_returns_dict(self):
        """Trend analysis returns a dictionary."""
        self.ledger.add_transaction("expense", "Lunch", 15.0, "2025-11-01")
        self.ledger.add_transaction("income", "Salary", 1000.0, "2025-11-01")
        trend = self.ledger.trend()
        self.assertIsInstance(trend, dict)


if __name__ == "__main__":
    unittest.main()
