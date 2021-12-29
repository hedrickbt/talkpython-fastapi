from typing import Optional


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    key = 'nope'
    q = f'{city},{country}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&units={units}'
    print(url)

