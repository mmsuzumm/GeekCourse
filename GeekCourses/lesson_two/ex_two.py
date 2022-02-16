given_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
temp_val = int  # Для избегания лишних ковычек при двух цифрах в строке
i = 0  # Не однобуквенная, а от iteration

while i < len(given_lst):  # Перебираем в цикле весь список
    for given_str in given_lst[i]:  # Рассматриваем каждую строчку в частности, чтобы найти цифры
        if '0' <= given_str <= '9':  # Находим число в строке
            if temp_val != i:  # Для определения двузначных и более чисел
                if len(given_lst[i]) == 1:
                    given_lst[i] = '0' + given_lst[i]  # Добавляем 0 для одной цифры
                elif given_lst[i][-1].isdigit() and not given_lst[i][-2].isdigit():  # Смотрим, 2 цифры, или 1
                    given_lst[i] = given_lst[i][0:-1] + '0' + given_lst[i][-1]  # Добавляем 0 для 1 цифры с символом
                given_lst[i] = '"' + given_lst[i] + '"'  # Добавляем кавычки
            temp_val = i
    i += 1

print(" ".join(given_lst))  # Выводим строку делая склейку через пробел
