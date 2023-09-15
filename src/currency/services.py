import requests

from src.conf import settings


def get_course(from_currency, to_currency) -> float:
    res = requests.get(f'{settings.currency_url}/{from_currency}/{to_currency}')
    res.raise_for_status()
    return res.json()


def convert(from_currency: str, to_currency: str, value: int) -> dict:
    try:
        course = get_course(from_currency, to_currency)
        return {'result': value * course}
    except Exception as e:
        return {'error': e}
