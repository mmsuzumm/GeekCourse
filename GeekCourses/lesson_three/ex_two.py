def num_translate_adv(num):
    check_first_num = num[0].isupper()  # Проверяем 1 букву на регистр
    num = num.lower()  # Делаем все буквы маленькими, для корректного поиска по словарю
    test_lst = {'zero': 'ноль',
                'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}  # Считаю уместно сделать dict локально, тк будет использоваться только для данной функции
    if check_first_num:  # Если первая буква заглавная, то
        print(test_lst.get(num).capitalize())  # При переводе на ру пишем с заглавной
    else:
        print(test_lst.get(num))  # Иначе с маленькой


if __name__ == '__main__':
    num_translate_adv('Three')
