class Monkey:
    def __init__(self, name, banana):
        self.name = name
        self.banana = banana
    def eat(self):
        print('Un singé nommé', self.name, 'mange une banane de couleur', self.banana.color)

class Banana:
    def __init__(self, color):
        self.color = color


banane_verte = Banana('verte')
banane_jaune = Banana('jaune')
Pierre = Monkey("Pierre", banane_jaune)
Marie = Monkey("Marie", banane_verte)

Pierre.eat()
Marie.eat()