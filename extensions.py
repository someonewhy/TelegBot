import requests
import json
from config import keys
class ConvertionExeption(Exception):
    pass


class CriptoConvektor:
    @staticmethod
    def get_price(quote: str,base: str ,amount: int):
        if quote == base:
            raise ConvertionExeption(f"Перевести {quote} в {base} невозможно.")
        try:
            quote_tikers = keys[quote]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {quote}")
        try:
            base_tikers = keys[base]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать количесвто {amount}")
        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {base}")
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_tikers}&tsyms={base_tikers}")
        total_base = json.loads(r.content)[keys[base]]
        try:
            total_base = total_base * amount
        except KeyError:
             raise ConvertionExeption(f"Не удалось вывести количесвто {amount}.")
        return  total_base
