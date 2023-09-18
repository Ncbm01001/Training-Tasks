#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
#и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    if month == 1 or month == 2 or month == 3:
        return ("Зима")
    elif month == 4 or month == 5 or month == 6:
        return ("Весна")
    elif month == 7 or month == 8 or month == 9:
        return("Лето")
    elif month == 10 or month == 11 or month == 12:
        return("Осень")
    else:
        return "Некорректный ввод"

print (season(99))
print (season(3))
print (season(7))
print (season(5))
print (season(11))
print (season(56))
