"""
Comprehensive Test Suite for Financial System ledger

Demonstrates:
- Unit testing for individual classes
- Integration testing for class interactions
- Test organization and best practices
- Using unittest framework (reinforces OOP with TestCase classes)
"""
import unittest
from finance_ledger import (
    AbstractTransaction,
    ExpenseTransaction,
    IncomeTransaction,
    FinanceLedger,
)


class TestInheritance(unittest.TestCase):
    """Test inheritance hierarchies."""

    def test_expense_is_abstract_transaction(self):
        expense = ExpenseTransaction(50.0, "2025-11-01", "Food")
        self.assertIsInstance(expense, AbstractTransaction)

    def test_income_is_abstract_transaction(self):
        income = IncomeTransaction(1000.0, "2025-1-05", "Payroll")
        self.assertIsInstance(income, AbstractTransaction)


class TestAbstractBaseClasses(unittest.TestCase):
    """Test abstract base class enforcement."""

    def test_cannot_instantiate_abstract_transaction(self):
        with self.assertRaises(TypeError):
            AbstractTransaction(50.0, "2025-11-01", "Test")


class TestPolymorphism(unittest.TestCase):
    """Test polymorphic behavior across transaction types."""

    def test_expense_impact_on_balance(self):
        expense = ExpenseTransaction(50.0, "2025-11-01", "Groceries")
        self.assertEqual(expense.impact_on_balance(), -50.0)

    def test_income_impact_on_balance(self):
        income = IncomeTransaction(1000.0, "2025-11-05", "Salary")
        self.assertEqual(income.impact_on_balance(), 1000.0)

    def test_transaction_type_property(self):
        expense = ExpenseTransaction(25.0, "2025-11-02", "Coffee")
        income = IncomeTransaction(500.0, "2025-11-03", "Payroll")
        self.assertEqual(expense.ttype, "expense")
        self.assertEqual(income.ttype, "income")


class TestTransactionValidation(unittest.TestCase):
    """Unit tests for transaction input validation."""

    def test_negative_expense_raises_error(self):
        with self.assertRaises(ValueError):
            ExpenseTransaction(-10.0, "2025-11-01", "Food")

    def test_negative_income_raises_error(self):
        with self.assertRaises(ValueError):
            IncomeTransaction(-100.0, "2025-11-01", "Salary")

    def test_zero_amount_raises_error(self):
        with self.assertRaises(ValueError):
            ExpenseTransaction(0.0, "2025-11-01", "Test")


class TestFinanceLedgerUnit(unittest.TestCase):
    """Unit tests for FinanceLedger behavior."""

    def setUp(self):
        self.ledger = FinanceLedger("Alex", {"food": 200, "entertainment": 80})

    def test_ledger_initialization(self):
        self.assertEqual(self.ledger.owner, "Alex")
        self.assertEqual(len(self.ledger.transactions), 0)

    def test_add_expense_transaction(self):
        tx = self.ledger.add_transaction("expense", "Lunch", 15.0, "2025-11-01")
        self.assertEqual(tx.ttype, "expense")
        self.assertEqual(len(self.ledger.transactions), 1)

    def test_add_income_transaction(self):
        tx = self.ledger.add_transaction("income", "Salary", 1000.0, "2025-11-01")
        self.assertEqual(tx.ttype, "income")

    def test_total_spent_empty_ledger(self):
        self.assertEqual(self.ledger.total_spent(), 0.0)

    def test_total_spent_only_expenses(self):
        self.ledger.add_transaction("expense", "Lunch", 15.0, "2015-11-01")
        self.ledger.add_transaction("expense", "Coffee", 5.0, "2025-12-01")
        self.assertEqual(self.ledger.total_spent(), 20.0)

    def test_search_no_results(self):
        self.ledger.add_transaction("income", "Salary", 1000.0, "2021-11-01")
        results = self.ledger.search("coffee")
        self.assertEqual(len(results), 0)

    def test_search_case_insensitive(self):
        self.ledger.add_transaction("expense", "Lunch at Cafe", 12.0, "2025-11-01")
        results = self.ledger.search("lUnCh")
        self.assertEqual(len(results), 1)


class TestFinanceLedgerAnalytics(unittest.TestCase):
    """Tests for summaries, trends, and analytics."""

    def setUp(self):
        self.ledger = FinanceLedger("Alex", {"food": 100})

    def test_month_summary_structure(self):
        summary = self.ledger.month_summary(2025, 11)
        self.assertIn("totals", summary)
        self.assertIn("budget_status", summary)

    def test_month_summary_with_expense(self):
        self.ledger.add_transaction("expense", "Dinner", 50.0, "2025-11-10")
        summary = self.ledger.month_summary(2025, 11)
        self.assertEqual(summary["totals"]["expense"], 50.0)

    def test_budget_over_limit(self):
        self.ledger.add_transaction("expense", "Groceries", 150.0, "2025-11-05")
        summary = self.ledger.month_summary(2025, 11)
        self.assertTrue(summary["budget_status"]["food"]["over_budget"])

    def test_top_categories_returns_list(self):
        self.ledger.add_transaction("expense", "Dinner", 50.0, "2025-11-10")
        self.ledger.add_transaction("expense", "Movie", 30.0, "2025-11-11")
        top = self.ledger.top_categories(2)
        self.assertIsInstance(top, list)
        self.assertEqual(len(top), 2)

    def test_trend_returns_dict(self):
        self.ledger.add_transaction("income", "Salary", 1000.0, "2025-11-01")
        trend = self.ledger.trend()
        self.assertIsInstance(trend, dict)


class TestFinanceLedgerIntegration(unittest.TestCase):
    """Integration tests for complete FinanceLedger workflows."""

    def test_complete_financial_workflow(self):
        ledger = FinanceLedger("Alex", {"food": 200})

        ledger.add_transaction("income", "Salary", 2000.0, "2025-11-01")
        ledger.add_transaction("expense", "Groceries", 150.0, "2025-11-02")
        ledger.add_transaction("expense", "Dining Out", 60.0, "2025-11-03")

        self.assertEqual(ledger.total_spent(), 210.0)

        summary = ledger.month_summary(2025, 11)
        self.assertIn("totals", summary)
        self.assertEqual(summary["totals"]["expense"], 210.0)

        search_results = ledger.search("grocer")
        self.assertEqual(len(search_results), 1)

    def test_recurring_transaction_detection(self):
        ledger = FinanceLedger("Alex", {})
        for i in range(3):
            ledger.add_transaction("expense", "Netflix", 15.0, f"2025-11-0{i+1}")
        recurring = ledger.detect_recurring(min_occurrences=3)
        self.assertTrue(len(recurring) > 0)


if __name__ == "__main__":
    unittest.main()

