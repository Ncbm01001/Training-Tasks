# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть;
# * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(num_1,num_2,oper):
    if oper == "+":
        return num_1 + num_2
    elif oper == "-":
        return num_1 - num_2
    elif oper == "*":
        return num_1 * num_2
    elif oper == "/":
        if num_2 == 0:
            print("На ноль делить нельзя")
        else:
            return num_1 / num_2
    else:
        print("Неизвестная операция")

print(arithmetic (1, 2, "х" ))
print(arithmetic (3, 4, "+" ))
print(arithmetic (5, 6, "-" ))
print(arithmetic (7, 8, "*" ))
print(arithmetic (9, 10, "/" ))
print(arithmetic (1, 0, "/" ))

