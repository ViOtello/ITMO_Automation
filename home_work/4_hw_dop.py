# ----------------------------------------------------------
# Задание № 4
# Доп*
# 4. В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
#       i.      Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
#       ii.     Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
#       iii.    Третий — присвоение автомобилю года выпуска.
#       iv.     Четвертый — присвоение автомобилю типа.
#       v.      Пятый — присвоение автомобилю цвета.

class Car:

    def __init__(self, color :str, type : str, year :int) -> str:
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return print('Автомобиль заведен')

    def stop(self):
        return print('Автомобиль заглушен')

    def year_of_car(self):
        return print('Год автомобиля - {}'.format(self.year))

    def type_of_car(self):
        return print('Тип автомобиля - {}'.format(self.type))

    def color_of_car(self):
        return print('Цвет автомобиля - {}'.format(self.color))

car_1 = Car('Красный', 'Хетчбек', '2007')
car_1.start()
car_1.stop()
car_1.year_of_car()
car_1.type_of_car()
car_1.color_of_car()
