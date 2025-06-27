# полиморфизм - это возможность использовать один интерфейс для разных типов данных.
# Полиморфизм позволяет использовать один и тот же метод для разных объектов.


class Animal:
    def speak(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def speak(self):
        print("Гав!")

class Cat(Animal):
    def speak(self):
        print("Мяу!")

def make_sound(animal):
    animal.speak()

make_sound(Dog())  # Гав!
make_sound(Cat())  # Мяу!


# Без наследования
class Car:
    def start(self):
        print("Машина поехала")

class Rocket:
    def start(self):
        print("Ракета взлетела!")

def launch(obj):
    obj.start()  # Не важно, Car или Rocket

launch(Car())     # Машина поехала
launch(Rocket())  # Ракета взлетела!
