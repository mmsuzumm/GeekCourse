price_lst = [10.0, 736.67, 37.02, 10.13, 14.14, 9999.99, 1, 1212.09, 190.91,
             33.33]  # Заполняем список при помощи генератора случайных чисел


def first_par():
    for prices in price_lst:
        rub = int(prices)
        penny = (prices - int(prices)) * 100
        print(f'{rub} руб {penny:02.0f} коп', end=', ')


# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).
def second_par():
    print(id(price_lst))
    price_lst.sort()
    print(id(price_lst))
    for prices in price_lst:
        prices_str = (int(prices * 100))
        prices_str = str(prices_str)
        print(f'{prices_str[0:-2]} руб {prices_str[-2:]} коп', end=', ')


# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
def third_par():
    price_lst = [10.0, 736.67, 37.02, 10.13, 14.14, 9999.99, 1, 1212.09, 190.91, 33.33]  # Переопределяем список
    # заново, тк работали с ним в функции 2, ну и по заданию
    for prices in sorted(price_lst, reverse=True)[::-1][
                  5::]:  # сортируем с реверсом, что создает перевернутый список и сразу переворачиваем его,
        # чтобы забрать самые большие числа

        rub = int(prices)
        penny = (prices - int(prices)) * 100
        print(f'{rub} руб {penny:02.0f} коп', end=', ')


if __name__ == '__main__':
    first_par()
    print('\n')
    second_par()
    print('\n')
    third_par()
