import sys
from os import remove

number = int(sys.argv[1]) - 1
new_val = (sys.argv[2])

bakery_temp = open('backery.txt', 'w+', encoding='UTF-8')  # w+ тк файл создается пустым
new_val_used = False  # Для отметки, было ли изменеие

with open('bakery.csv', 'r+', encoding='UTF-8') as bakery_f:  # r+ тк файл открывается для чтения и есть возможность
    # записи
    for idx, line in enumerate(bakery_f):
        if idx == number:  # Когда номер указаной строки совпадает с номером строки в файле
            bakery_temp.write(f'{new_val}\n')  # то заменяем эту строку во временном файле на указанную пользователем
            new_val_used = True  # Если изменение было, то отмечаем это

        else:
            bakery_temp.write(line)  # иначе просто копируем строку из актуального файла

    if not new_val_used:
        bakery_temp.close()
        remove('backery.txt')
        exit('Такой строки нет')  # Если указана строка, чей номер больше, чем есть строк в файле - выходим из
        # скрипта

    bakery_temp.seek(0)

with open('bakery.csv', 'w', encoding='UTF-8') as bakery_f:
    for line in bakery_temp:
        bakery_f.write(line)

bakery_temp.close()
remove('backery.txt')
