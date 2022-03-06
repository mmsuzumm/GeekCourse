import sys

arguments = sys.argv[1:]
with open('bakery.csv', encoding='UTF-8') as bakery_f:
    if len(arguments) == 0:
        start_i = 0
        end_i = sum(1 for line in bakery_f)
        bakery_f.seek(0)
    elif len(arguments) == 1:
        start_i = int(arguments[0])
        end_i = sum(1 for line in bakery_f)
        bakery_f.seek(0)
    else:
        start_i = int(arguments[0])
        end_i = int(arguments[1])

    for idx, line in enumerate(bakery_f):
        if start_i <= idx+1 <= end_i:
            print(line.strip())