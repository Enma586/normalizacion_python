# Normalizer module for transforming transaction data

import json
from config import currency_mapping, status_mapping, date_format_patterns
from datetime import datetime

def normalize_transaction(transaction):
    source = ""
    normalized_transaction = {}

    if "id" in transaction:
        source = "Source A"
        normalized_transaction["id"] = transaction["id"]
        normalized_transaction["amount"] = float(transaction["amount"].replace(",", "."))
        normalized_transaction["currency"] = currency_mapping.get(transaction["currency"].lower(), transaction["currency"].upper())
        normalized_transaction["timestamp"] = datetime.strptime(transaction["timestamp"], date_format_patterns[0]).isoformat()
        normalized_transaction["status"] = status_mapping.get(transaction["status"].lower(), "FAILED")
    elif "transaction_id" in transaction:
        source = "Source B"
        normalized_transaction["id"] = f"tx_{transaction['transaction_id']}"
        normalized_transaction["amount"] = transaction["total"] / 100.0
        normalized_transaction["currency"] = currency_mapping.get(transaction["currency_code"].lower(), transaction["currency_code"].upper())
        normalized_transaction["timestamp"] = datetime.strptime(transaction["created_at"], date_format_patterns[1]).isoformat()
        normalized_transaction["status"] = status_mapping.get(transaction["state"].lower(), "FAILED")
    elif "ref" in transaction:
        source = "Source C"
        normalized_transaction["id"] = transaction["ref"]
        normalized_transaction["amount"] = float(transaction["amount"].replace("€", "").replace(",", "."))
        normalized_transaction["currency"] = "EUR"
        normalized_transaction["timestamp"] = datetime.fromisoformat(transaction["date"].replace("Z", "+00:00")).isoformat()
        normalized_transaction["status"] = status_mapping.get(transaction["result"].lower(), "FAILED")

    normalized_transaction["source"] = source
    return normalized_transaction

def load_transactions(file_path):
    with open(file_path, 'r') as file:
        transactions = json.load(file)
    return transactions

def save_normalized_transactions(transactions, output_file):
    with open(output_file, 'w') as file:
        json.dump(transactions, file, indent=4)