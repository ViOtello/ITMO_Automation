def task_1(a: int, b: float, c: str, d: list, f: bool) -> tuple:
    return a, b, c, d, f


a = 11
b = 12.324254
c = 'gaz'
d = [123, 23, 45, 64]
f = True

print(task_1(a, b, c, d, f), type(task_1(a, b, c, d, f)))

for elem in task_1(a, b, c, d, f):
    print(elem, type(elem))
print('\n')

#######################################################################

def task_2(a_2: list = [1, 2, 3, 5, 8, 13, 21])-> int:
    return a_2[0:3] # вывод трех элементов списка

print('a_2[0:3] = ', task_2())
print('\n')
# d. * - скажите как называется эта последовательность чисел
# пункт задания d. не понятен, как и суть написанной функции

#######################################################################

def task_3(square: int) -> int:
    return square**2

square = 6
print(task_3(square))
square = 2.2
print(task_3(square))

#######################################################################