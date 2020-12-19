"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""
import os
import random
import string


def create_file(name):
    if os.path.isfile(name):
        print('Такой файл уже создан')
    else:
        with open(name, 'w', encoding='utf-8') as text_file:
            numbers = [random.randint(1,100) for x in range(10)]
            words = [''.join(random.choice(string.ascii_lowercase) for x in range(10)) for y in range(10)]
            text_file.writelines([f'{number} {word}\n' for number, word in zip(numbers, words)])
            return text_file


def read_file(name):
    with open(name, 'r', encoding='utf-8') as txt:
        for line in txt:
            print(line)


create_file('text.txt')
read_file('text.txt')  # не получается сделать открытие через дескриптор, поэтому временно оставляю так
