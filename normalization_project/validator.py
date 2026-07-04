# Validator module for checking transaction integrity

def validate_transaction(transaction):
    required_fields = ["id", "amount", "currency", "timestamp", "status"]
    for field in required_fields:
        if field not in transaction:
            return False, f"Missing field: {field}"
    
    if not isinstance(transaction["amount"], (int, float)) or transaction["amount"] < 0:
        return False, "Invalid amount"
    
    return True, ""

def separate_invalid_transactions(transactions):
    valid_transactions = []
    invalid_transactions = []

    for transaction in transactions:
        is_valid, reason = validate_transaction(transaction)
        if is_valid:
            valid_transactions.append(transaction)
        else:
            transaction["error"] = reason
            invalid_transactions.append(transaction)

    return valid_transactions, invalid_transactions
