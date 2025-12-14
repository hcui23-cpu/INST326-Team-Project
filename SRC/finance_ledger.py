
import json

class FinanceLedger:
    def __init__(self, owner, budgets=None):
        self.owner = owner
        self.transactions = []
        self.budgets = budgets or {}

    def save_to_json(self, filename):
        data = {
            "owner": self.owner,
            "budgets": self.budgets,
            "transactions": self.transactions
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, "r") as f:
            data = json.load(f)

        ledger = cls(data["owner"], data["budgets"])
        ledger.transactions = data["transactions"]
        return ledger
