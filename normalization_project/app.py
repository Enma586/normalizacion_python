# Main application for the interactive interface

import json
from normalizer import load_transactions, save_normalized_transactions
from validator import separate_invalid_transactions
from metrics import calculate_metrics

import streamlit as st

def main():
    st.title("Sistema de Normalización de Transacciones")
    st.write("Por favor, pega tu archivo JSON de transacciones aquí:")
    
    # Display expected format
    st.markdown("""
    **Formato Esperado:**
    ```json
    [
        {
            "id": "tx_001",
            "amount": "100.50",
            "currency": "USD",
            "timestamp": "2025-03-10 14:22:00",
            "status": "completed"
        },
        ...
    ]
    ```
    """)
    
    json_input = st.text_area("Datos JSON:")
    
    if st.button("Procesar"):
        if json_input:
            try:
                transactions = json.loads(json_input)
                valid_transactions, invalid_transactions = separate_invalid_transactions(transactions)
                normalized_transactions = [normalize_transaction(tx) for tx in valid_transactions]

                output_file = "normalized_transactions.json"
                save_normalized_transactions(normalized_transactions, output_file)

                st.write("Transacciones Normalizadas:")
                st.json(normalized_transactions)

                metrics = calculate_metrics(normalized_transactions)

                st.write("\nMétricas:")
                st.write(f"Total de Transacciones: {metrics['total_transactions']}")
                st.write(f"Transacciones Válidas: {metrics['valid_count']}")
                st.write(f"Transacciones Inválidas: {metrics['invalid_count']}")
                for currency, total in metrics['currency_totals'].items():
                    st.write(f"Total {currency}: {total:.2f}")

                if invalid_transactions:
                    st.write("\nTransacciones Inválidas:")
                    st.json(invalid_transactions)
            except json.JSONDecodeError:
                st.error("Error: El JSON proporcionado no es válido.")

if __name__ == "__main__":
    main()