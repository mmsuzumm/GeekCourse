file_name = 'nginx_logs.txt'

with open(file_name) as f:
    test_dict = {}
    temp_max = 0
    for line in f:
        remote_addr = line[:line.find(' - -')]
        test_dict.setdefault(remote_addr, 0)
        test_dict[remote_addr] += 1 # заполняем словарь и подсчитываем количество созданных запросов для каждого пользователя

for temp_r in test_dict:
    if test_dict[temp_r] == max(test_dict.values()): # достаем ключ пользователя с наибольшим количеством вопросов
        spammer = f'{temp_r}' # Это и будет наш спамер

print(spammer)
