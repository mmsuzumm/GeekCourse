from random import randint


def get_jokes(**kwargs):  # По заданию надо сделать через именованные аргументы
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    iteration = 0  # Переменная для выхода из цикла while
    lst_of_jokes = []  # Лист для записи шуток
    while iteration < kwargs.get('num_of_jokes'):  # Цикл нужeн для вывода нескольких шуток
        first_word = nouns[randint(0, len(nouns) - 1)]  # Берем слово из 1 списка
        # Мне казалось, что randint работает по принципу ("первое значение" , "последнее значение, не учитывая его"),
        # оказалось поледнее значение учитывается, поэтому "-1"
        second_word = adverbs[randint(0, len(adverbs) - 1)]  # Берем слово из 2 списка
        third_word = adjectives[randint(0, len(adjectives) - 1)]  # Берем слово из 3 списка
        the_joke = f'{first_word} {second_word} {third_word}'  # Пишем шутку
        if kwargs.get('repetition'):  # Если второй аргумент есть, то
            nouns.remove(first_word)  # убираем использованное значение из 1 списка
            adverbs.remove(second_word)  # убираем использованное значение из 2 списка
            adjectives.remove(third_word)  # убираем использованное значение из 3 списка
        lst_of_jokes.append(the_joke)  # Заносим ее в словарь
        iteration += 1

    return lst_of_jokes  # Возвращаем список шуток в функцию


if __name__ == '__main__':
    print(get_jokes(num_of_jokes=5, repetition=True))  # По заданию надо сделать через именованные аргументы
