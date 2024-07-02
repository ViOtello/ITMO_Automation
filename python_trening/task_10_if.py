# программа проверяет число положительное или отрицательное

num_0 = 3
num_1 = -5
num_2 = 0

if num_1 >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


#____________________________________________________________________


#Задача str_2 содержит в себе str_1?

def yes_no(str_1, str_2):
    if str_1 in str_2:
        print(True)
    else:
        print(False)

yes_no(str_1 = 'test', str_2 = 'test1')


#____________________________________________________________________


num_float = 3.4
# num_float = 0
# num_float = -123.7

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

#____________________________________________________________________


permit_print = True

if (num_0 > 0 and permit_print):
    print('num ', num_0, ' - положительное число')
elif not permit_print:
    print('Печать запрещена')


# ____________________________________________________________________

def student_rank(year_of_study):
    if year_of_study >= 1 and year_of_study <= 4:
        print('Вы бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы магистр')
    elif 7 <= year_of_study <= 9:
        print('Вы аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(7)

# ____________________________________________________________________

num_a = 5

if num_a > 100 or num_a < -100:
    print('-')
else:
    print('+')