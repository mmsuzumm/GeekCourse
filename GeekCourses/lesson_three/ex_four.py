def thesaurus_adv(*args):
    names_dict = {}
    for names in args:  # Перебираем имена
        dict_key = names.split(' ')[-1][0]  # Берем первую букву фамилии, разбивая строку на 2 слова, беря первую
        # букву последнего элемента
        dict_key_two = names.split(' ')[0][0]  # Берем первую букву имени, разбивая строку на 2 слова, беря первую
        # букву первого элемента
        names_dict.setdefault(dict_key, {})  # Создаем словарь по этому ключу
        names_dict[dict_key].setdefault(dict_key_two, [])  # Создаем ключ по первой букве фамилии
        names_dict[dict_key][dict_key_two].append(names)  # Находим определенный ключ в ключе, записываем имя по
        # первой букве имени()

    return names_dict


if __name__ == '__main__':
    print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
