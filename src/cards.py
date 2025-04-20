import os

import pandas as pd


def read_transactions_excel(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel"""
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    else:
        df = df.fillna("")
        transactions = df.to_dict("records")
        return transactions


default_path = os.path.join("..", "data", "operations.xls")


def get_last_digits(transactions: list[dict]) -> list[dict]:
    """Извлекает последние 4 цифры номера карты из списка транзакций."""
    result = []
    for transaction in transactions:
        card_number = str(transaction.get("Номер карты", "")).strip()

        if not card_number:
            continue

        digits = "".join(c for c in card_number if c.isdigit())

        if len(digits) >= 4:
            result.append({"last_digits": digits[-4:]})

    return result


def calculate_total_expenses(transactions: list[dict]) -> float:
    """Вычисляет общую сумму расходов из списка транзакций"""
    total_expenses = 0.0

    for transaction in transactions:
        amount = transaction.get("Сумма операции", 0.0)
        if amount < 0:
            total_expenses += abs(amount)

    return total_expenses


def calculate_cashback(transactions: list[dict]) -> float:
    """Считает кешбэк (1 рубль за каждые 100 рублей)"""
    cashback = 0.0

    for transaction in transactions:
        amount = transaction.get("Сумма операции", 0.0)
        if amount < 0:
            cashback += abs(amount) // 100

    return cashback
