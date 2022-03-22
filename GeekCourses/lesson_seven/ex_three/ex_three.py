import os
import shutil

core_folder = 'my_project'

z = next(os.walk(core_folder))[0]
try:
    os.mkdir(f'{os.getcwd()}\\{core_folder}\\templates')
except FileExistsError:
    pass

for idx in os.walk(core_folder):
    if 'templates' in idx[0]:  # Все что находится в templates - и есть наши шаблоны
        for k in idx[-1]:
            path = f'{os.getcwd()}\\{idx[0]}\\'  # Путь к папке, которую надо скопировать изначально
            path_lst = path.split('\\')  # Делаем список из пути к файлу, чтобы найти необходимую папку
            temp_to_file = '\\'.join(path_lst[path_lst.index('templates'):-1])  # Находим путь до файла, начиная с templates
            try:  # Тк мы не знаем сколько будет файлов обработаем try except на случай если их будет больше 1,
                # Так же это поможет если создан уже есть 1 или 2 файла.
                shutil.copytree(f'{path}', f'{os.getcwd()}\\{z}\\{temp_to_file}')
            except FileExistsError:
                pass
