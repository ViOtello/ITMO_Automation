# определяем функцию
def add(x, y): # add- название функции, в () - тело функции
    return x + y

# вызываем функцию
# add(1, 2)

print(add(1, 2))

print(add('I a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a+b+c+d

print(arg(1,1,1,1))

print(arg(2,2))

print(arg(1,1,1))

print(arg(2, 2, 0.3, 1)) # float отрабатывается как дроби и целых чисел
# однако если мы на место аргумента запишем строку- нам выдаст ошибку

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1','2','3','4'))

print(range_arg('1', '2', d='3', c='4'))