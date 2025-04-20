from datetime import datetime


def get_greeting() -> str:
    """
    Функция для приветствия пользователя в зависимости от времени суток.
    """
    current_time = datetime.now().hour

    if 5 <= current_time < 12:
        return "Доброе утро"
    elif 12 <= current_time < 17:
        return "Добрый день"
    elif 17 <= current_time < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
print(get_greeting())
