# Configuration for mappings and constants
currency_mapping = {
    "usd": "USD",
    "eur": "EUR",
    # Add more mappings as needed
}

status_mapping = {
    "completed": "SUCCESS",
    "OK": "SUCCESS",
    "success": "SUCCESS",
    "failed": "FAILED",
    "pending": "PENDING",
    # Add more mappings as needed
}

date_format_patterns = [
    "%Y-%m-%d %H:%M:%S",  # YYYY-MM-DD HH:MM:SS
    "%d/%m/%Y %H:%M",     # DD/MM/YYYY HH:MM
    "%Y-%m-%dT%H:%M:%SZ", # ISO-8601
]