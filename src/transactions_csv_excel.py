from typing import Any, Dict

import pandas as pd


def transactions_csv(file: str) -> list[Dict[str, Any]]:
    """Функция для считывания финансовых транзакций из CSV."""
    df = pd.read_csv(file, sep=';')
    return df.to_dict(orient='records')


def transactions_excel(file_path: str) -> list[Dict[str, Any]]:
    """Функция для считывания финансовых транзакций из Excel."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
