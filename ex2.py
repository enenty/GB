"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""
import os


def print_directory_contents(sPath):
    def get_content(sPath):
        name_and_path = []
        for content in os.listdir(sPath):
            full_name = os.path.join(os.path.abspath(sPath), content)
            if os.path.isfile(full_name):
                name_and_path.append((os.path.abspath(sPath), content))
            else:
                name_and_path.extend(get_content(full_name))
        return name_and_path

    for i in get_content(sPath):
        print(i)


print_directory_contents('C:\\Program Files\Git')
