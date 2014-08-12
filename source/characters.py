import random

#A rudimentary class that stores the character's position and health
class Character(object):
    def __init__(self, posx, posy, c):
        self.health = 5
        self.posx = posx
        self.posy = posy
        self.c = c

    def getpos(self):
        return (self.posx, self.posy)

    def attack(self, opponent):
        if random.random() > 0.5:
            self.health -= 1
        else:
            opponent.health -= 1



