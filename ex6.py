"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReportFirst(ItemDiscount):
    def __str__(self):
        return f'{self.get_info}'

    @property
    def get_info(self):
        return f'{self.get_name()}'


class ItemDiscountReportSecond(ItemDiscount):
    def __str__(self):
        return f'{self.get_info}'

    @property
    def get_info(self):
        return f'{self.get_price()}'


first = ItemDiscountReportFirst('name', 100)
second = ItemDiscountReportSecond('price', 100)

print(first)
print(second)

print(first.get_info)
print(second.get_info)



