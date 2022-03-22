def gen(given_num):
    num_gen = (num for num in range(1, given_num, 2))
    return num_gen


gen_5 = gen(22)
print(type(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))
print(next(gen_5))