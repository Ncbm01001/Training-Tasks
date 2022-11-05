# Задание 2

# Напишите функцию *time_metric_down(time, metric, metric_down)*, которая на вход принимает три значения:
# - time - количество единиц времени, целое число;
# - metric - единица измерения времени ('w', 'd', 'h', 'm');
# - metric_down - в какой единице измерения необходимо получить результат ('d', 'h', 'm', 's');
# В этой задаче metric_down является меньшей единицей измерения, чем metric.
# Пример реализации функции:
# *time_metric_down(10, 'h', 's')**>>> 36000*
# Т.е. в 10 часах содержится 36000 секунд.

def time_metric_down(time, metric, metric_down):

    if  metric not in ['w', 'd', 'h', 'm']:
        print("Некорректный ввод")
    if metric_down not in ['d', 'h', 'm', 's']:
        print ("Некорректный ввод")

    if metric == "w" and metric_down == "d":
        metric_down = time * 7
    if metric == "w" and metric_down == "h":
        metric_down = time * 7 * 24
    if metric == "w" and metric_down == "m":
        metric_down = time * 7 * 24 * 60
    if metric == "w" and metric_down == "s":
        metric_down = time * 7 * 24 * 60 * 60

    if metric == "d" and metric_down == "d":
        metric_down = time
    if metric == "d" and metric_down == "h":
        metric_down = time * 24
    if metric == "d" and metric_down == "m":
        metric_down = time * 24 * 60
    if metric == "d" and metric_down == "s":
        metric_down = time * 24 * 60 * 60

    if metric == "h" and metric_down == "d":
        metric_down = time / 24
    if metric == "h" and metric_down == "h":
        metric_down = time
    if metric == "h" and metric_down == "m":
        metric_down = time * 60
    if metric == "h" and metric_down == "s":
        metric_down = time * 60 * 60

    if metric == "m" and metric_down == "d":
        metric_down = time / 60 / 24
    if metric == "m" and metric_down == "h":
        metric_down = time / 60
    if metric == "m" and metric_down == "m":
        metric_down = time
    if metric == "m" and metric_down == "s":
        metric_down = time * 60
    return metric_down


#Проверка
print(time_metric_down(1, "w", "w"))
print(time_metric_down(1, "w", "d"))
print(time_metric_down(14, "h", "d"))
print(time_metric_down(652, "m", "d"))


