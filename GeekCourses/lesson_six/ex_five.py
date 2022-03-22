import sys
from itertools import zip_longest

general = sys.argv[1]
user_f = sys.argv[2]
hobby_f = sys.argv[3]

user_f = open(user_f, encoding='UTF-8')
hobby_f = open(hobby_f, encoding='UTF-8')

num_user = sum(1 for row in user_f)
num_hobby = sum(1 for row in hobby_f)

if num_hobby > num_user:
    raise SystemExit(1)

user_f.seek(0)
hobby_f.seek(0)

with open(general, 'w', encoding='UTF-8') as general_f:
    for line_user, line_hobby in zip_longest(user_f, hobby_f):  # Мы используем цикл for вместо того, чтобы целиком открыть файл
        general_f.write(f'{line_user.strip().split(",")}: '
                        f'{line_hobby.strip().split(",") if line_hobby is not None else line_hobby}\n')

user_f.close()
hobby_f.close()
