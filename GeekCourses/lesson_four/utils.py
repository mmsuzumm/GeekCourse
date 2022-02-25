import requests
from decimal import Decimal
from datetime import datetime


def current_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency not in response:
        return None

    rubles = response[response.find('<Value>', response.find(currency)) + 7:response.find('</Value>', response.find(currency))]  # Находим стоимость в XML
    date_of = response[response.find('Date="') + 6: response.find('" name=')]  # Дата

    day, month, year = int(date_of.split(".")[0]), int(date_of.split(".")[1]), int(date_of.split(".")[2])
    # Расписываем дату по отдельным переменным для работы с datetime
    date_of = datetime(day=day, month=month, year=year).date()  # Переводим из datetime в date

    return f'{float(Decimal(rubles.replace(",", ".")))}, {date_of}'  # Используем Decimal вместо конструкции с
    # переводом в лист и обратно в строку


if __name__ == '__main__':
    current_rates('USD')
    current_rates('EUR')
    current_rates('something')
