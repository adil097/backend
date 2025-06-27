# функции могут быть вложенными (замыкания) - 
# это функции, которые определены внутри других функций,
# и они могут использовать переменные из внешней функции.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
# Вызов вложенной функции
inner_func_variable = outer_function(10)
result = inner_func_variable(5)  # 15
# ТЕПЕРЬ inner_func_variable - это типа как

def inner_function(y):
        return 10 + y


