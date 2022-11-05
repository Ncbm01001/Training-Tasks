# Задание №1
# Требуется определить количество рабочих часов четырех сотрудников работающих по графику 2 через 2 по 12 часов.
# Первый работник приступает к работе первого числа, второй - второго, третий - третьего, а четвертый - четвертого.
# Рассматриваемый период - февраль. Праздники отсутствуют.
#
# Результатом выполнения кода должна быть информация о том,
# сколько часов каждый из сотрудников отработал за месяц, а также общее количество отработанных часов.

# Важный дисклеймер. Прочитав задание я решил, что условные четыре человека работают по очереди  друг за другом.
# Так же я решил добавить остальные месяцы, ибо мне писать это все понравилось)
# Позже, погда все это написал, посмотрел твое решение и оказалось, что я усложнил себе задачу.

print(
    "1 — январь, 2 — февраль, 3 — март,\n4 — апрель, 5 — май, 6 — июнь,\n7 — июль, 8 — август, 9 — сентябрь,\n10 — октябрь, 11 — ноябрь, 12 — декабрь\nВведите порядковый номер месяца:")

day_in_months = [1, 31, 2, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_numder_function = int(input())

while (months_numder_function > 12) or (months_numder_function < 1):
    print("Некорректный ввод. Воспользуйтесь справкой выше и попробуйте еще раз.")
    months_numder_function = int(input())

month = day_in_months[months_numder_function]

while months_numder_function == 2:
    print("Интересующий вас год высокосный? Ответьте, пожалуйста, словами <Да> или <Нет>.")
    leap_year = input()
    if (leap_year == "Да") or (leap_year == "да"):
        month = 29
        months_numder_function = 3
    elif (leap_year == "Нет") or (leap_year == "нет"):
        month = 28
        months_numder_function = 3
    else:
        print("Некорректный ввод. Попробуйте, пожалуйста, еще раз.")

total_working_time = month * 12
print("Общее рабочее время этом месяце составляет", total_working_time, "ч.")
first_worker = 0
second_worker = 0
third_worker = 0
fourth_worker = 0

while total_working_time > 0:
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    first_worker = first_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    first_worker = first_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    second_worker = second_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    second_worker = second_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    third_worker = third_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    third_worker = third_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    fourth_worker = fourth_worker + 12
    if total_working_time < 1:
        break
    total_working_time = total_working_time - 12
    fourth_worker = fourth_worker + 12

print("Первый рабочий отработал в этом месяце", first_worker, "ч.")
print("Второй рабочий отработал в этом месяце", second_worker, "ч.")
print("Третий рабочий отработал в этом месяце", third_worker, "ч.")
print("Четвертый рабочий отработал в этом месяце", fourth_worker, "ч.")
