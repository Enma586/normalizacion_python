# Metrics module for calculating statistics

def calculate_metrics(transactions):
    total_transactions = len(transactions)
    valid_count = sum(1 for t in transactions if "error" not in t)
    invalid_count = total_transactions - valid_count

    currency_totals = {}
    for transaction in transactions:
        if "error" not in transaction:
            currency = transaction["currency"]
            amount = transaction["amount"]
            if currency in currency_totals:
                currency_totals[currency] += amount
            else:
                currency_totals[currency] = amount

    return {
        "total_transactions": total_transactions,
        "valid_count": valid_count,
        "invalid_count": invalid_count,
        "currency_totals": currency_totals
    }
