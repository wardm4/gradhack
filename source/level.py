import random, characters
from characters import Character
from characters import Enemy

characters.Character = Character
characters.Enemy = Enemy

class Level(object):
    def __init__(self, start, dlvl):
        self.xsize = 50
        self.ysize = 25
        self.start = start
        self.numenemy = random.randint(1,5)
        self.enemylist = []
        self.corridor = randwalk(self.start)
        for i in range(self.numenemy):
        	r = random.randint(1,3000)
        	self.enemylist.append(Enemy(self.corridor[r][0], self.corridor[r][1], 'v', 'virus'))
        n = random.randint(1,3000)
        self.end = (self.corridor[n][0], self.corridor[n][1])

    def getx(self, n):
    	return self.corridor[n][0]

    def gety(self, n):
    	return self.corridor[n][1]

    def legalspace(self,x,y):
	    tmp2 = True
	    for enemy in self.enemylist:
	        tmp2 = (tmp2 and (x,y) != enemy.getpos())
	    return tmp2 and (x,y) in self.corridor
    			


def randx():
    return random.randint(11,59)

def randy(): 
    return random.randint(6, 29)

def randwalk(start):
	a = [start]
	current = start
	for i in range(3000):
		r = random.random()
		if r < 0.25:
			if current[0] < 58:
				current = (current[0] + 1, current[1])
		if 0.25 < r and r < 0.5:
			if current[0] > 11:
				current = (current[0] - 1, current[1])
		if r > 0.5 and r < 0.75:
			if current[1] < 28:
				current = (current[0], current[1] + 1)
		if r > 0.75:
			if current[1] > 6:
				current = (current[0], current[1] - 1)
		a.append(current)
	return a




