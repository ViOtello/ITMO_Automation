class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        return "Переход по url - {}".format(self.url)
        # print(self.url) - как на видео

home = Page('https://www.youtube.com/watch?v=MXuFm5Vsw6M&t=376s')

print(home.get())
print('\n\n\n')