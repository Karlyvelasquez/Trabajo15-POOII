import requests

class APIConsumo:
    def __init__(self, url):
        self.url = url

    def Consumo(self):
        response = requests.get(self.url)
        response.raise_for_status()
        data = response.json()
        return data