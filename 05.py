# Сколько цифр Х будет в числе Y
print("Введите цифру для поиска")
search_number = input()
print("Введите число, в котором будет происходить поиск")
big_number = input()
total = 0
for i in range(1, int(big_number)+1):
    index = str(i).find(str(search_number))
    total += index+1
print(total)