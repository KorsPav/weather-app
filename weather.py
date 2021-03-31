import requests
import json
from constants import API_KEY


class Weather:

    def __init__(self, city):
        self._city = city

    def _gen_url(self):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self._city}&appid={API_KEY}&units=metric'
        return url

    def get_temp(self):
        city_url = self._gen_url()
        response = requests.get(city_url)
        if response.status_code == 200:
            content = json.loads(response.content)
            return content['main']['temp']
        else:
            content = json.loads(response.content)
            raise ValueError(f'{content["cod"]} error')
