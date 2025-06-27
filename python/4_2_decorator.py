# Декоратор - это функция, которая принимает другую функцию 
# и расширяет ее функциональность без изменения ее кода.


def decorator_function(func):
    def wrapper():
        print("decorator function started!")
        func()
        print("dcorator function finished!")
    return wrapper


@decorator_function
def original_function():
    print("original function do the code")


original_function() # decorator function started! original function do the code decorator function finished!

