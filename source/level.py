import random, characters
from characters import Character as Character

class Level(object):
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.numenemy = random.randint(1,5)
        self.enemylist = []
        for i in range(self.numenemy):
            self.enemylist.append(Character(randx(), randy(), 'v'))

def randx():
    return random.randint(11,59)

def randy(): 
    return random.randint(6, 29)