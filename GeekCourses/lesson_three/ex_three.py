def thesaurus(*args):
    names_dict = {}
    for names in args:  # Перебираем имена
        dict_key = names[0]  # Берем первую букву
        dict_val = names  # Записываем имя в отдельную переменную
        names_dict.setdefault(dict_key, [])  # Создаем список по этому ключу
        names_dict[dict_key].append(dict_val)  # Записываем имя по ключу

    return names_dict


if __name__ == '__main__':
    print(thesaurus('Иван', 'Артем', 'Стёпа', 'Вася', 'Андрей', 'Алексей', 'Петр', 'Понтий'))
