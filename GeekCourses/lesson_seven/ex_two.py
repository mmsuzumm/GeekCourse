import os


def check_tab(word):
    checker = 0
    for idx in range((len(word)//4)):
        if '    ' in word:
            checker += 1
            word = word[4:]
    return checker
# Подсчитывает сколько tab'ов в строке


def func_create(word):
    if '.' in word:
        f = open(word, 'w', encoding='UTF-8')
        f.close
    else:
        try:
            os.mkdir(word)
        except FileExistsError:
            print(f'папка с таким {word} именем уже существует')


config_f = open('config.yaml', encoding='UTF-8')
path = os.getcwd()
create_lst = [item[:-1] for item in config_f]
temp_check_tab = -1
for item in create_lst:
    tab_counter = 0
    if check_tab(item) > temp_check_tab:

        path = f'{path}\\{item[check_tab(item)*4:]}'  # Указываем путь до файла/папки
        print(path)
        func_create(path)
    elif check_tab(item) < temp_check_tab:
        for i in range(temp_check_tab - check_tab(item) + 1):
            path = path[::-1]
            path = path[path[1:].find('\\') + 1:]
            path = path[::-1]
        path = f'{path}{item[check_tab(item) * 4:]}'  # Указываем путь до файла/папки
        print(path)
        func_create(path)
    elif check_tab(item) == temp_check_tab:
        path = path[::-1]
        path = path[path[1:].find('\\') + 1:]
        path = path[::-1]
        path = f'{path}{item[check_tab(item) * 4:]}'
        print(path)
        func_create(path)
    print(item[check_tab(item)*4:])

    temp_item = item[check_tab(item)*4:]

    temp_check_tab = check_tab(item)  # Временная переменная для хранения предыдущего значения табуляции


config_f.close()