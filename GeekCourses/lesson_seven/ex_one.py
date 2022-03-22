import os
import sys


def create_structure(root_directory='my_project', folder_lst=['settings', 'mainapp', 'adminapp', 'authapp']):  # по
    # умолчанию передается ряд параметров, соответствеющих  стартеру проекта

    input_data = sys.argv[1:]

    if len(input_data) == 1:
        root_directory = str(input_data[0])  # данная структура необходима для избегания проблем с отсутствием
        # аргрументов
    elif len(input_data) > 1:  # Если аргументов больше 1 то берем все аргументы кроме первого как папки
        root_directory = str(input_data[0])
        folder_lst.extend(input_data[1:])

    for value in folder_lst:
        if os.path.exists(os.getcwd() + f'\\{root_directory}\\{value}') is False:
            os.makedirs(os.getcwd() + f'\\{root_directory}\\{value}')  # Создаем папки по указанным путям
        else:
            print(f'папка {root_directory}\\{value} уже существует')


if __name__ == '__main__':
    create_structure()