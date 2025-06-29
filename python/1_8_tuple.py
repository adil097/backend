# кортеж (tuple) - это неизменяемый (immutable) тип данных, 
# который позволяет хранить несколько значений в одной переменной
# кортежи создаются с помощью круглых скобок
# кортежи могут содержать элементы разных типов
coords = (50.45, 30.52)
point = (1,)              # кортеж из одного элемента (запятая обязательна!)
empty = ()                # пустой кортеж


# Доступ к элементам кортежа
coords[0]  # 50.45
coords[-1] # 30.52
coords[:1]  # (50.45,)


x, y = coords
print(x)  # 50.45
print(y)  # 30.52
