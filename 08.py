#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
#(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def square (side):
    perimeter = f"Периметр - {side*4}"
    area = f"Периметр - {side**2}"
    diagonal = f"диагональ - {math.sqrt(2 * side * side)}"
    return (perimeter, area, diagonal)

print (square(2))
print (square(5))
print (square(27))
print (square(63))
print (square(123))