#Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.

def is_year_leap (year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return (True)
    else:
        return (False)

print (is_year_leap(1925))
print (is_year_leap(1861))
print (is_year_leap(1756))
print (is_year_leap(1428))
print (is_year_leap(1358))
print (is_year_leap(1147))
print (is_year_leap(1))
print (is_year_leap(2))
print (is_year_leap(3))
print (is_year_leap(4))

