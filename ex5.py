"""
5. Реализовать расчет цены товара со скидкой.

Величина скидки должна передаваться в качестве аргумента в дочерний класс.

Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.

В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой.

Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы
(вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, name, price, discount):
        ItemDiscount.__init__(self, name, price)
        self.discount = discount

    def __str__(self):
        price_disc = ((self.get_price()) / 100) * self.discount
        return f'{self.get_name()} {self.get_price() - price_disc}'

    def get_parent_data(self):
        print(self.get_name(), self.get_price())


item = ItemDiscountReport('name', 100, 10)
item.new_price(77)
item.get_parent_data()
print(item)
