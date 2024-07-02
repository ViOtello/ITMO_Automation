# Задание № 1
# Cоздайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
#       i. расчет площади прямоугольника
#       ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


Rectangle_1 = Rectangle(5, 12)
Rectangle_2 = Rectangle(10, 10)
Rectangle_3 = Rectangle(2, 4)
print(Rectangle_1.area(), Rectangle_1.perimeter())
print(Rectangle_2.area(), Rectangle_2.perimeter())
print(Rectangle_3.area(), Rectangle_3.perimeter())
print('\n')


# ------------------------------------------------------------
# Задание № 2
# 2. Создайте класс Math.
#   a. Создайте два атрибута — a и b.
#   b. Напишите методы
#       i. addition — сложение,
#       ii. multiplication — умножение,
#       iii. division — деление,
#       iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить
# соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self):
        return print('Сложение - ', self.a + self.b)

    def multiplication(self):
        return print('Умножение - ', self.a * self.b)

    def division(self):
        if self.b == 0:
            print('На ноль делить нельзя')
        else:
            print('Деление с остатком - ', self.a / self.b)
            print('Деление без остатка - ', self.a // self.b)

    def subtraction(self):
        return print('Вычитание - ', self.a - self.b)


m_1 = Math(12, 4)
m_1.addition()
m_1.multiplication()
m_1.division()
m_1.subtraction()
print('\n')

m_2 = Math(-12, 4)
m_2.addition()
m_2.multiplication()
m_2.division()
m_2.subtraction()
print('\n')

m_3 = Math(0, 4)
m_3.addition()
m_3.multiplication()
m_3.division()
m_3.subtraction()
print('\n')

m_4 = Math(4, 0)
m_4.addition()
m_4.multiplication()
m_4.division()
m_4.subtraction()
print('\n')


# ----------------------------------------------------------
# Задание № 3
# На странице https://demoqa.com/text-box присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class SidebarElements:

    def __init__(self, text: str, type: str, loc: str) -> str:
        self.text = text
        self.type = type = 'Кнопка'
        self.loc = loc

    def print(self):
        return print(self.type + ' - ' + self.text + ' имеет локатор ' + self.loc)

    def click(self):
        return print("Клик по кнопке - {}".format(self.text) + '\n')


text_box = SidebarElements('Text Box', type, loc='SidebarElements#text_box')
text_box.print()
text_box.click()

check_box = SidebarElements('Check Box', type, loc='SidebarElements#check_box')
check_box.print()
check_box.click()

radio_button = SidebarElements('Radio Button', type, loc='SidebarElements#radio_button')
radio_button.print()
radio_button.click()

web_tables = SidebarElements('Web Tables', type, loc='SidebarElements#web_tables')
web_tables.print()
web_tables.click()

buttons = SidebarElements('Buttons', type, loc='SidebarElements#buttons')
buttons.print()
buttons.click()

links = SidebarElements('Links', type, loc='SidebarElements#links')
links.print()
links.click()

broken_links_images = SidebarElements('Broken Links - Images', type, loc='SidebarElements#broken_links_images')
broken_links_images.print()
broken_links_images.click()

upload_and_download = SidebarElements('Upload adn Download', type, loc='SidebarElements#upload_and_download')
upload_and_download.print()
upload_and_download.click()

dynamic_properties = SidebarElements('Dynamic Properties', type, loc='SidebarElements#dynamic_properties')
dynamic_properties.print()
dynamic_properties.click()

