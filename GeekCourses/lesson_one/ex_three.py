def percents_work():

    percents_in = int(input('Введите число от 0 до 100 включительно\n'))

    p = percents_in % 10

    if p == 1 and percents_in != 11:
        percent_str = 'процент'
    elif 10 <= percents_in <= 19:
        percent_str = 'процентов'
    elif 2 <= p <= 4:
        percent_str = 'процента'
    elif 5 <= p <= 9 or p == 0:
        percent_str = 'процентов'

    print(f'{percents_in} {percent_str}')


if __name__ == '__main__':
    percents_work()
