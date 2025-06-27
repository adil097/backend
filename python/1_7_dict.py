# Объявление словаря - это неупорядоченная коллекция пар ключ-значение.
person = {
    "name": "Adil",
    "age": 27,
    "is_student": False
}

empty = {}


# Доступ к элементам словаря
print(person["name"])   # Adil
print(person.get("age"))  # 27
print(person.get("city", "Astana"))  # "Astana", если ключа нет

# Изменение элемента словаря
person["age"] = 28           # меняем значение
person["city"] = "Almaty"    # добавляем новый ключ

# Удаление элемента словаря
del person["is_student"]  # удаляем элемент по ключу
person.pop("age")        # удаляем элемент по ключу и возвращаем значение
person.clear()          # очищаем словарь

# Методы словаря
# Получение всех ключей
keys = person.keys()  # dict_keys(['name', 'city'])
# Получение всех значений
values = person.values()  # dict_values(['Adil', 'Almaty'])
# Получение всех пар ключ-значение
items = person.items()  # dict_items([('name', 'Adil'), ('city', 'Almaty')])
# Безопасное получение значения по ключу
value = person.get("age", "Unknown")  # "Unknown", если ключа нет
# Обновление словаря
person.update({"age": 28, "is_student": True})  # обновляем словарь

# Цикл по словарю
for key in person:
    print(key, person[key])

# или
for key, value in person.items():
    print(f"{key}: {value}")

# Проверка наличия ключа в словаре
"name" in person       # True
"salary" in person    # False

# Вложенные словари
users = {
    "adil": {"age": 27, "city": "Astana"},
    "timur": {"age": 25, "city": "Almaty"}
}

print(users["adil"]["city"])  # Astana

