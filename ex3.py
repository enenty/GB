"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)
"""
import random as rand


def rand_generator(first, last, length):
    rand_list = []
    rand_dict = {}
    for el in range(length+1):
        number = rand.randrange(first, last + 1)
        while number not in rand_list:
            rand_list.append(number)
            rand_dict.update({f'elem_{number}': number})
            break

    print(rand_list)
    print(rand_dict)
    

rand_generator(3, 10, 4)





