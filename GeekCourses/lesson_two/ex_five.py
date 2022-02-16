from random import uniform

price_lst = [round(uniform(0.01, 100000.00), 2) for i in
             range(21)]  # Заполняем список при помощи генератора случайных чисел

for prices in price_lst:
    prices = (int(prices * 100))  # Переводим все в int, чтобы убрать точку, а последние 2 цифры станут копейками\
    # можно не домножать на 100, а разбить сплитом по точке позже
    prices_str = str(prices)  # Дальше легко будет все обработать в строке, тк мы знаем, что копейки максимум
    # двузначное число.

    print(f'{prices_str[0:-2]} руб {prices_str[-2:]} коп')

# Работает при условии, что 82.5 это 82 рубля 50 копеек, а не 82 рубля 5 копеек, тк так работает float. Или я не
# понял как сделать задание.