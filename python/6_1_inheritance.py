# Наследование - это механизм, позволяющий создавать новый класс на основе существующего. 
# Новый класс наследует свойства и методы родительского класса, 
# что позволяет избежать дублирования кода и улучшить его структуру.

class Parent:
    def say_hello(self):
        print("Привет от родителя!")

class Child(Parent):
    pass

child = Child()
child.say_hello()  # Наследованный метод


# Можно поменять поведение метода в дочернем классе, переопределив его.
class Parent:
    def say_hello(self):
        print("Привет от родителя!")
class Child(Parent):
    def say_hello(self):
        print("Привет от ребенка!")

child = Child()
child.say_hello()  # Переопределенный метод

# Можно использовать метод родительского класса в дочернем классе с помощью super()

class Parent:
    def say_hello(self):
        print("Привет от родителя!")
class Child(Parent):
    def say_hello(self):
        super().say_hello()  # Вызов метода родительского класса
        print("Привет от ребенка!")  # Дополнительное поведение

child = Child()
child.say_hello()  # Привет от родителя! Привет от ребенка!

# __init__ в наследуемом классе
class Parent:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Привет от родителя {self.name}!")
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.age = age
    def say_hello(self):
        super().say_hello()  # Вызов метода родительского класса
        print(f"Привет от ребенка {self.name}, мне {self.age} лет!")  # Дополнительное поведение



#Множественное наследование

class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

# Вывод: 