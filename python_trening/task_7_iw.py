def task_func(a=(1, 2, 3, 4)): # передаем в тело функции кортеж неизменяемый
    return a[0] #выводим первый элемент кортежа

print(task_func()) # просто активируем функцию


def compute_surface(radius, pi=3.14159): # радиус -переменная которую дальше введем, пи - по умолчанию
    return pi * radius * radius # выводим счет по формуле

print(compute_surface(2)) #2-это радиус