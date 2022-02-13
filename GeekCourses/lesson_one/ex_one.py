def rework():
    seconds = int(input('Введите время в секундах\n'))

    d = 'дн'
    h = 'час'
    m = 'мин'
    s = 'сек'

    days = seconds // 86400  # Вычисляю сколько дней
    seconds -= days * 86400  # Вычисляю сколько секунд осталось после вычета дней
    hours = seconds // 60 // 60  # Вычисляю часы
    seconds -= hours * 3600  # Вычисляю сколько секунд осталось после вычета часов
    minutes = seconds // 60  # Вычисляю минуты
    seconds -= minutes * 60  # Вычисляю сколько секунд осталось после вычета минут

    if days:
        print(f'{days} {d} {hours} {h} {minutes} {m} {seconds} {s}')
    elif hours:
        print(f'{hours} {h} {minutes} {m} {seconds} {s}')
    elif minutes:
        print(f'{minutes} {m} {seconds} {s}')
    elif seconds:
        print(f'{seconds} {s}')


if __name__ == '__main__':
    rework()
