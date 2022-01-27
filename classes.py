class Cat:

    Name_Class = 'Кошки'

    def __init__(self, wool_color, eyes_color, name):
        self.wool_color = wool_color
        self.eyes_color = eyes_color
        self.name = name

    def purr(self):
        print('Мурррр!')

    def hiss(self):
        print('ШШШШ!')

    def scrabble(self):
        print("Црп!")

my_cat = Cat('Белая', 'Зелёные','Мурка')
print('Наименование класса - ', my_cat.Name_Class)
print('Вот наша кошка: ')
print('Цвет шерсти - ', my_cat.wool_color)
print('Кличка - ', my_cat.name)