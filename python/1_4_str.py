# Строки в Python
# Объявление строк
name = "Adil"
greeting = 'Hello'
multiline = """Это
многострочная
строка"""

# Строки можно объединять
greeting = greeting + " " + name
# Или так
greeting += " " + name
# Или так
greeting = f"{greeting} {name}"

# Строки можно умножать
greeting = greeting * 3 #  "Hello Adil Hello Adil Hello Adil"
# индексация строк
greeting[0] # "H"
# срезы строк
greeting[0:5] # "Hello"
greeting[0:5:2] # "Hlo"
# длина строки
len(greeting) # 15
# Строки можно сравнивать
greeting == "Hello Adil Hello Adil Hello Adil" # True

#Методы строк
# Приведение к нижнему регистру
greeting.lower() # "hello adil hello adil hello adil"
# Приведение к верхнему регистру
greeting.upper() # "HELLO ADIL HELLO ADIL HELLO ADIL"
# Удаление пробелов в начале и конце строки
greeting.strip() # "Hello Adil Hello Adil Hello Adil"
# Замена подстроки
greeting.replace("Adil", "Ali") # "Hello Ali Hello Ali Hello Ali"
# Разделение строки на список
greeting.split() # ["Hello", "Adil", "Hello", "Adil", "Hello", "Adil"]
# Объединение списка строк в одну строку
greeting_list = ["Hello", "Adil", "Hello", "Adil", "Hello", "Adil"]
# Строки можно объединять
greeting = " ".join(greeting_list) # "Hello Adil Hello Adil Hello Adil"
# Поиск подстроки
greeting.find("Adil") # 6
# Поиск подстроки с конца
greeting.rfind("Adil") # 18
# Проверка цифры в строке
greeting.isdigit() # False
# Проверка буквы в строке
greeting.isalpha() # False
# Проверка пробела в строке
greeting.isspace() # False