"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""
import os
import random
import string
import re


def create_file(name):
    if os.path.isfile(name):
        print('Такой файл уже создан')
    else:
        with open(name, 'w+', encoding='utf-8') as old_file:
            numbers = [random.randint(1,100) for x in range(10)]
            words = [''.join(random.choice(string.ascii_lowercase) for x in range(10)) for y in range(10)]
            old_file.writelines([f'{number} {word}\n' for number, word in zip(numbers, words)])
        with open(name, 'r', encoding='utf-8') as file, open('new_file.txt', 'w+', encoding='utf-8') as new_file:
            for line in file:
                list_line = line.split(' ')
                new_line = re.sub(list_line[0], list_line[-1], line)
                new_file.write(f'{new_line}\n')


def read_file(name):
    with open(name, 'r', encoding='utf-8') as txt:
        for line in txt:
            print(line)


create_file('text121.txt')
read_file('text121.txt')  # не получается сделать открытие через дескриптор, поэтому временно оставляю так
