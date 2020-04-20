class Monkey:
    def __init__(self, name, banane):
        self.name = name
        self.banane = banane
    def mange(self):
        print('Un singé nommé', self.name, 'mange une banane de couleur', self.banane.color)

class Banane:
    def __init__(self, color):
        self.color = color


banane_verte = Banane('verte')
banane_jaune = Banane('jaune')
Pierre = Monkey("Pierre", banane_jaune)
Marie = Monkey("Marie", banane_verte)

Pierre.mange()
Marie.mange()