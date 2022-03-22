def gen(given_num):
    for num in range(1, given_num, 2):
        yield num


gen_5 = gen(5)
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
