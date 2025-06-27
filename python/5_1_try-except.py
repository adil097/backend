# Исключения в Python

try:
    print("Пытаемся выполнить код")
except Exception as e:
    print(f"Не получилось, вот ошибка: {e}")
else:
    print("Получилось! Ошибок не произошло")
finally:
    print("Мы закончили")



# except может ловить определённые ошибки
try:
    print("Пытаемся выполнить код")
except ZeroDivisionError as e: # ловим деление на ноль
    print(f"Деление на 0: {e}")
except ValueError as e: # ловим ошибку значения
    print(f"Ошибка значения: {e}")
except IndexError as e:
    print(f"Ошибка индекса: {e}")
except TypeError as e:
    print(f"Ошибка типа: {e}")
except KeyError as e:
    print(f"Ошибка ключа: {e}") 
except AttributeError as e:
    print(f"Ошибка атрибута: {e}")
except FileNotFoundError as e:
    print(f"Файл не найден: {e}")
except IOError as e:
    print(f"Ошибка ввода-вывода: {e}")
except ImportError as e:
    print(f"Ошибка импорта: {e}")
except NameError as e:
    print(f"Ошибка имени: {e}")
except AssertionError as e:
    print(f"Ошибка утверждения: {e}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
else:
    print("Получилось! Ошибок не произошло")
finally:
    print("Мы закончили")

x = 5
try:
    x = x + 5
    x = x / 0  # деление на ноль
except ZeroDivisionError as e:
    print(f"Ошибка деления на ноль: {e}")

print(x)  # x будет равно 10, а не 5 