src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 199, 200]


def sort_out():  # Создаем генератор
    for number in src:
        yield number


sort = sort_out()
result = []
next(sort)  # Пропуск 1 шага генератора

for num in src:
    if num == src[-1]:  # Если последни символ, то выходим для избегания ошибки
        continue
    number_next = next(sort)
    if number_next > num:
        result.append(number_next)

print(result)
