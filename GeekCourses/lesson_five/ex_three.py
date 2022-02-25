tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen():
    for num in range(0, len(tutors)):
        if num+1 > len(klasses):
            tuple_creator = (tutors[num], None)  # В случае если tutors > klasses то вернется (<tutors>, None)
        else:
            tuple_creator = (tutors[num], klasses[num])  # Иначе вернется (<tutors>, <klasses>)
        yield tuple_creator


tuple_gen = my_gen()

print(type(tuple_gen))  # Проверяем, что это действительно генератор

print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))