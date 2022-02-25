import requests
from decimal import Decimal
from datetime import datetime


def current_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if currency not in response:
        return None  # Если в строке нет запоршенной валюты - возвращаем None
    rubles = response[response.find('<Value>', response.find(currency)) + 7:response.find('</Value>', response.find(currency))]  # Находим валюту... Сложно

    print(f'{float(Decimal(rubles.replace(",", ".")))}') # Используем Decimal вместо конструкции с переводом в лист и обратно в строку


    # rubles = rubles.split(',')            # Использован float
    # rubles = float('.'.join(rubles))      # Использован float
    # print(rubles)                         # Использован float
    # print(type(rubles))                   # Использован float

if __name__ == '__main__':
    current_rates('USD')
    current_rates('EUR')
    current_rates('something')