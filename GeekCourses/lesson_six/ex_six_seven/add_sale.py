import sys

with open('bakery.csv', 'a', encoding='UTF-8') as bakery_f:
    add = sys.argv[1]
    bakery_f.write(f'{add} \n')
