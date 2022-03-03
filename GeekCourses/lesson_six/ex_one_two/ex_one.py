file_name = 'nginx_logs.txt'
my_parser = []
with open(file_name) as f:
    for line in f:
        remote_addr = line[:line.find(' - -')]
        request_type = line[line.find('"')+1:line.find(' ', line.find('"'))]
        requested_resource = line[line.find('', line.find(request_type))+len(request_type)+1:line.find('"', line.find(request_type))]
# remote_addr - легко
# request_type - ищем первое слово от ".
# request_resourse начиная от request_type до " исключая сам request_type, а так же +1 делаем для убирания пробела
        lst_of_tuple = (remote_addr, request_type, requested_resource)  # получаем кортеж для каждой строки
        my_parser.append(lst_of_tuple)  # заносим все полученные кортежи в список
print(my_parser)
