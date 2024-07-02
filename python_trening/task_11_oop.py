class Button: # class - ключевое слово создания класса
              # Button - имя класса с заглавной буквы!

    type: str = 'Кнопка' # атрибут класса

    def __init__(self, text, link): # тело класса пишутся с отступом подстрок
        self.text = text
        self.link = link
        # def __init__(self) - это конструктор класса - это
        # стандартный метод для объявления атрибутов. Это метод инициализатор,
        # который запускается сразу после создания объектов
        # self. - это внутренний обьект класса, как указатель
        # он передается во всех методах и во всех атрибутах первым всегда


# Создаем экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам .. осуществляется через точку
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class Button_Two:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

# Создаем экземпляры класса
home_two = Button_Two('Домой', '/home', 'button#home')

# Вызываем метод
print(home_two.click())
print('\n\n\n')
# ------------------------------------------------------------------

class Input:

    def __init__(self, Loc):
        self.Loc = Loc

search = Input ('Input#search')

print(search.Loc)
print('\n\n\n')
