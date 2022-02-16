numbers_lst = [i ** 3 for i in range(1, 1001) if
               i % 2 != 0]  # а еще можно указать шаг "2" в аргументе для функции "range"
second_num_lst = []


def first_calc():
    for number in numbers_lst:
        res = 0  # переменная для вычисления суммы цифр в числе
        save_num = number  # сохраняем изначальное число в отдельную переменную
        while save_num:
            res += save_num % 10
            save_num //= 10

        if res % 7 == 0:
            second_num_lst.append(number)  # заполняем массив числами, подходящими по условию

    print(sum(second_num_lst))


def second_calc():
    sum_of_num = 0
    for number in numbers_lst:
        res = 0  # переменная для вычисления суммы цифр в числе
        save_num = number  # сохраняем изначальное число в отдельную переменную
        save_num += 17
        while save_num:
            res += save_num % 10
            save_num //= 10

        if res % 7 == 0:
            sum_of_num += number  # сразу считаем число внутри цикла

    print(sum_of_num)


if __name__ == '__main__':
    first_calc()
    second_calc()
