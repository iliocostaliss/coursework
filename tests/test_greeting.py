from unittest.mock import patch

from src.greeting import get_greeting


def test_morning_greeting():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.hour = 5
        assert get_greeting() == "Доброе утро"
        mock_datetime.now.return_value.hour = 11
        assert get_greeting() == "Доброе утро"


def test_evening_greeting():
    with patch("src.greeting.datetime") as mock_datetime:
        mock_datetime.now.return_value.hour = 17
        assert get_greeting() == "Добрый вечер"

        mock_datetime.now.return_value.hour = 22
        assert get_greeting() == "Добрый вечер"


def test_boundary_cases():
    with patch("src.greeting.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.hour = 4
        assert get_greeting() == "Доброй ночи"

        mock_now.hour = 5
        assert get_greeting() == "Доброе утро"

        mock_now.hour = 12
        assert get_greeting() == "Добрый день"

        mock_now.hour = 17
        assert get_greeting() == "Добрый вечер"

        mock_now.hour = 23
        assert get_greeting() == "Доброй ночи"
