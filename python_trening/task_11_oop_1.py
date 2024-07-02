# ------------------------------------------------------------------
from task_11_checks import Checks
class Input(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

search = Input ('Локатор', ' Input#search')
print(search.text + search.loc)
search.check_text(search.loc)

class Button(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

search_2 = Button ('Локатор', ' Button#search')
print(search_2.text + search_2.loc)
search_2.check_text(search_2.loc)

class Title(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

search_3 = Title ('Локатор', ' Title#search')
print(search_3.text + search_3.loc)
search_3.check_text(search_3.loc)

class Link(Checks):
    def __init__(self, text, link):
        self.text = text
        self.link = link

search_4 = Link ('Ссылка ', ' /Link/cmsdfmksdmfksdm')
print(search_4.text + search_4.link)
print('\n\n\n')