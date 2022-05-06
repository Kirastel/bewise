import requests
from datetime import datetime


def jservice_request(num):
    url = f'https://jservice.io/api/random?count={num}'
    response = requests.get(url)
    data = response.json()
    return (data)


def date_conversion(str_date: str) -> str:
    PATTERN_IN = "%Y-%m-%dT%H:%M:%S.%fZ"
    PATTERN_OUT = "%Y-%m-%d"

    date = datetime.strptime(str_date, PATTERN_IN)

    return (datetime.strftime(date, PATTERN_OUT))


