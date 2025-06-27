# Инкапсуляция - это механизм, который позволяет скрыть внутреннюю реализацию
# класса и предоставить только необходимый интерфейс для взаимодействия с ним.

class Person:
    def __init__(self, name, age, ethnicity):
        self.name = name  # публичный атрибут
        self._age = age    # защищенный атрибут
        self.__ethnicity = ethnicity  # приватный атрибут 

    def get_name(self):  # метод доступа к публичному атрибуту
        return self.name
    
    def get_age(self):  # метод доступа к приватному атрибуту
        return self._age

    def set_ethnicity(self):  # метод изменения приватного атрибута
        return self.__ethnicity
    
    # можно на методы

    def _hidden():
        print("Это защищенный метод")

    def __really_hidden():
        print("Это приватный метод")




# Геттеры и сеттеры - это методы, которые позволяют получать и изменять значения
# атрибутов класса. Они обеспечивают контроль над доступом к атрибутам и
# позволяют выполнять дополнительные действия при получении или изменении значений.


class Product:
    def __init__(self, price):
        self._price = price  # защищённый

    @property
    def price(self):  # геттер
        return self._price

    @price.setter
    def price(self, value):  # сеттер
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

p = Product(100)
print(p.price)     # ✅ Геттер
p.price = 150      # ✅ Сеттер
# p.price = -50    # ❌ Ошибка: цена не может быть отрицательной
