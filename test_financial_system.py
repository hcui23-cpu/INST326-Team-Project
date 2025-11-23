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
