import csv
from itertools import zip_longest
users_dict = {}
i = 0

users_f = open('users.csv', encoding='UTF-8')
hobby_f = open('hobby.csv', encoding='UTF-8')

csv_user = csv.reader(users_f)
csv_hobby = csv.reader(hobby_f)

row_count_u = sum(1 for row in csv_user)  # Считаем количество строк в пользователях
row_count_h = sum(1 for row in csv_hobby)  # Считаем количество строк в хобби

if row_count_u < row_count_h:
    raise SystemExit(1)  # В случае если в хобби больше строк - завершаем программу

users_f.seek(0)
hobby_f.seek(0)

users_lst = list(zip_longest(csv_user, csv_hobby))
for name in users_lst:
    users_dict[' '.join(name[0])] = name[1]  # Заполняем словарь
    with open('general.txt', 'w', encoding='UTF-8') as general:
        for key, val in users_dict.items():
            general.write('{}: {}\n'.format(key, val))  # какой тип файла должен быть на выходе не написано, поэтому сделал простым путем, в txt

hobby_f.close()
users_f.close()
