from abc import ABC, abstractmethod


class PaymentMethod(ABC):  # Абстрактный класс
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата {amount} тенге картой")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата {amount} тенге через PayPal")

def checkout(payment: PaymentMethod):
    payment.pay(1000)

checkout(CreditCard())  # Оплата 1000 тенге картой
checkout(PayPal())      # Оплата 1000 тенге через PayPal
