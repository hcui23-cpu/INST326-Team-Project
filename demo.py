"""
Personal Finance Tracker - Interactive Demo
Demonstrates a complete information system workflow
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from finance_ledger import (
    AbstractTransaction,
    ExpenseTransaction,
    IncomeTransaction,
    FinanceLedger
)


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def main():
    """Run the finance tracking system demo."""

    print_section("Personal Finance Tracker – System Demonstration")
    print("\nThis walkthrough highlights:")
    print("  • Object-oriented design principles")
    print("  • Abstract base classes and polymorphism")
    print("  • Composition and system coordination")
    print("  • Reuse of functional components")
    print("  • End-to-end workflow integration")

    # ======================================================================
    # Step 1: Create a Ledger Instance
    # ======================================================================
    print_section("Step 1: Create a User Ledger")

    ledger = FinanceLedger(
        owner="Jordan",
        category_budgets={
            "food": 250.0,
            "transportation": 120.0,
            "subscriptions": 60.0
        }
    )

    print(f"\nLedger initialized:")
    print(f"  {ledger}")
    print(f"  Owner: {ledger.owner}")
    print(f"  Monthly budgets: {ledger.category_budgets}")

    # ======================================================================
    # Step 2: Abstract Class Validation
    # ======================================================================
    print_section("Step 2: Abstract Base Class Validation")

    print("\nTesting abstract class behavior:")
    try:
        AbstractTransaction(30, "2025-10-15", "Test Transaction")
    except TypeError as err:
        print(f"  ✓ AbstractTransaction cannot be instantiated: {err}")

    # ======================================================================
    # Step 3: Transaction Types (Inheritance & Polymorphism)
    # ======================================================================
    print_section("Step 3: Transaction Types")

    rent = ExpenseTransaction(850.00, "2025-10-01", "Monthly rent")
    paycheck = IncomeTransaction(2100.00, "2025-10-05", "Biweekly paycheck")

    print("\nTransaction examples:")
    print(f"  Expense → {rent.description}, impact: {rent.impact_on_balance()}")
    print(f"  Income  → {paycheck.description}, impact: {paycheck.impact_on_balance()}")

    # ======================================================================
    # Step 4: Recording Transactions (Composition)
    # ======================================================================
    print_section("Step 4: Recording Transactions")

    ledger.add_transaction("expense", "Gas station", 45.30, "2025-10-06")
    ledger.add_transaction("expense", "Grocery store", 96.75, "2025-10-07")
    ledger.add_transaction("income", "Tutoring payment", 300.00, "2025-10-08")
    ledger.add_transaction("expense", "Streaming service", 12.99, "2025-10-09")

    print("\nLedger transaction records:")
    for entry in ledger.transactions:
        print(f"  {entry}")

    # ======================================================================
    # Step 5: Spending Analysis
    # ======================================================================
    print_section("Step 5: Spending Analysis")

    spent = ledger.total_spent()
    print(f"\nTotal expenses recorded: ${spent:.2f}")

    print("\nSearching for 'grocery':")
    for match in ledger.search("grocery"):
        print(f"  Found: {match['description']} (${match['amount']})")

    # ======================================================================
    # Step 6: Monthly Overview & Budgets
    # ======================================================================
    print_section("Step 6: Monthly Overview")

    overview = ledger.month_summary(2025, 10)

    print("\nSpending by category:")
    for category, amount in overview["totals"].items():
        print(f"  {category}: ${amount:.2f}")

    print("\nBudget usage:")
    for category, info in overview["budget_status"].items():
        print(f"  {category}: {info['status']} "
              f"({info['percent_used']:.1f}% of budget used)")

    # ======================================================================
    # Step 7: Highest Expense Categories
    # ======================================================================
    print_section("Step 7: Highest Expense Categories")

    for cat, amt in ledger.top_categories(2):
        print(f"  {cat}: ${amt:.2f}")

    # ======================================================================
    # Step 8: Detecting Recurring Charges
    # ======================================================================
    print_section("Step 8: Detecting Recurring Charges")

    for date in ["2025-10-01", "2025-10-08", "2025-10-15"]:
        ledger.add_transaction("expense", "Gym Membership", 29.99, date)

    recurring = ledger.detect_recurring(min_occurrences=3)

    if recurring:
        print("\nRecurring transactions identified:")
        for item in recurring:
            print(f"  {item}")
    else:
        print("\nNo recurring charges found")

    # ======================================================================
    # Step 9: Trend Reporting
    # ======================================================================
    print_section("Step 9: Trend Reporting")

    trends = ledger.trend()
    print("\nTrend summary:")
    for key, value in trends.items():
        print(f"  {key}: {value}")

    # ======================================================================
    # Conclusion
    # ======================================================================
    print_section("Demo Finished")

    print("\nKey takeaways:")
    print("  ✓ Encapsulation through private ledger state")
    print("  ✓ Inheritance and polymorphism via transactions")
    print("  ✓ Abstract base class enforcement")
    print("  ✓ Composition of transactions within a ledger")
    print("  ✓ Functional reuse from earlier project stages")
    print("  ✓ Fully integrated information system")

    print("\nThis finance tracking system is complete and ready for submission.")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

