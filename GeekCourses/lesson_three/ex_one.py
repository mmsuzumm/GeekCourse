def num_translate(num):
    num = num.lower()
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

    print(test_lst.get(num))
    return test_lst.get(num)


if __name__ == '__main__':
    num_translate('Two')
