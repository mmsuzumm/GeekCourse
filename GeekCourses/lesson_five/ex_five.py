src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

sort = (number for number in src)  # Создаем генератор проходящи по циклу src

num_dict = {}
result = []

for counter in range(0, len(src)):  # цикл для каждого значения в списке
    num = next(sort)
    num_dict.setdefault(num, [])  # Создаем словарь для дальнейшей оптимизации
    num_dict[num].append(num)
for key in num_dict.keys():
    if len(num_dict[key]) == 1:
        result.append(key)

print(result)