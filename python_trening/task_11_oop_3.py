# Мой вариант решения
class Soda_my:

    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            return "Газировка и {}".format(self.additive)
        elif self.additive == 0:
            return "Обычная газировка"

water = Soda_my('лимон')
print(water.show_my_drink())

water_2 = Soda_my(0)
print(water_2.show_my_drink())
print('\n')

# Правильное решение:
class Soda:

    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}') # при таком написании пишется f
        else:
            print('Обычная газировка')

drink_1 = Soda()
drink_2 = Soda('Малина')
drink_1.show_my_drink()
drink_2.show_my_drink()