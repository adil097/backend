# циклы (for, while)

# примеры использования циклов while
i = 0
while i < 5:
    print(i)
    i += 1

# пример использования циклов for
for i in range(5):
    print(i)


# пример использования циклов for с условием break и continue
for i in range(5):
    if i == 3:
        break # прерывает цикл
    print(i)  # 0, 1, 2

for i in range(5):
    if i == 3:
        continue # пропускает итерацию
    print(i)  # 0, 1, 2, 4

# пример использования цикла for с else
# else выполняется, если цикл завершился без break
for i in range(5):
    if i == 10:
        break
else:
    print("Цикл прошёл до конца")

# вложенные циклы
for i in range(3):
    for j in range(2):
        print(i, j)
