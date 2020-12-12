"""
4. Реализовать возможность переустановки значения цены товара.

Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def new_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.get_name(), self.get_price())


item = ItemDiscountReport('name', 100)
item.new_price(77)
item.get_parent_data()
