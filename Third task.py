# Задание 3
# n! - это факториал числа n, т.е. произведение всех целых чисел от 1 до n включительно. 0!=1
# Требуется реализовать не менее, чем тремя способами, нахождение *n!* и определить эффективный
# способ расчета. Реализовать код необходимо через функцию *fctrl(n)*, в которую подается число n.
# Можно использовать любое количество дополнительных функций. После нахождения эффективного метода
# расчета факториала числа n, нужно переписать код в функцию *best_fctrl(n)*.
# Один из способов обязательно должен использовать библиотеку math.
# Можете пробовать использовать различные встроенные или внешние библиотеки,
# рекурсию, циклы. Замер скорости исполнения нужно проводить на достаточно
# большом значении аргумента n, например, при n=1000

import math
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np

#Option №1
def factorial1(n):
    fact_1 = math.factorial(n)
    return fact_1
print (factorial1(1000)) #Check


#Option №2
def factorial2(n):
    x = 1
    y = 1
    while x < n:
        y = x * y
        x = x + 1
        if x == n:
            return y
print (factorial2(1000)) #Check


#Option №3
def factorial3(n):
    q = (range(1, n+1))
    w = 1
    for e in range(len(q)):
        w = w * q[e]
    return w
print (factorial3(1000)) #Check

func = ["factorial1", "factorial2", "factorial3"]
time = []
if __name__ == '__main__':
    for j in func:
        time.append(timeit(j+'(1000)', setup = 'from __main__ import '+j, number = 1000))

time = np.array(time)
time = time*100/time.max()

for i, j in zip(func, time):
    print(i, '-', str(round(j,2))+'%')

plt.bar(func, time)
plt.show()


# Проверка из задания
def best_fctrl(n):
    return factorial1(n)
if (best_fctrl(0) == 1 and best_fctrl(1) == 1 and best_fctrl(2) == 2 and best_fctrl(3) == 6 and
    best_fctrl(10) == 3628800):
    print('Ошибки не выявлены')
else:
    print('Выявлены ошибки')