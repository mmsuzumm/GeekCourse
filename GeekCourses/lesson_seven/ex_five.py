import os
core_folder = os.getcwd()

weight_lst = []
counter = 0
biggest_file = 0
dict_weight = {}
file_type = []
tuple_for_dict = ()

for item in os.walk(core_folder):
    if item[-1]:
        for value in item[-1]:
            weight_lst.append(os.stat(f'{item[0]}\\{value}').st_size)  # Создаем список веса всех файлов которые есть
            file_type.append(value[value.find('.') + 1:])
            # в папке и подпапках
            # print(f'{item[0]}\\{value}')

max_weight = max(weight_lst)  # Самое большое значение из списка

while max_weight >= 1:
    max_weight = max_weight // 10
    counter += 1  # Находим количество цифр в числе

for value in range(counter):
    if biggest_file == 0:
        biggest_file = 10
    else:
        biggest_file *= 10
# Находим наибольшее значение для ключа


while biggest_file > 0:
    counter_quantity = 0
    idx_for_type = 0
    temp_type_lst = []
    for value in weight_lst:
        if biggest_file/10 <= value < biggest_file:
            counter_quantity += 1
            temp_type_lst.append(file_type[idx_for_type])  # Создаем список с всеми типами файлов
            temp_type_lst = set(temp_type_lst)  # Избавляемся от повторов
            temp_type_lst = list(temp_type_lst)  # Избавляемся от повторов
            tuple_for_dict = (counter_quantity, temp_type_lst)  # Собираем кортдеж из количества файлов и типов данных
            dict_weight[int(biggest_file)] = tuple_for_dict  # Итоговый результат
        idx_for_type += 1
    biggest_file /= 10


for key, value in dict_weight.items():
    value_tuple = value
    print(f'{key} : {value_tuple}')  # Выводим на печать в удобном формате
