import random, characters, book, item, io
from characters import Character
from characters import Enemy
from book import Book
from item import Item

characters.Character = Character
characters.Enemy = Enemy
book.Book = Book
item.Item = Item

#Random placement function
def rp():
	return random.randint(1, 3000)

class Level(object):
    def __init__(self, start, dlvl, book, item, hero):
        self.xsize = 50
        self.ysize = 25
        self.start = start
        self.numenemy = random.randint(1,5)
        self.enemylist = []
        self.corridor = randwalk(self.start)
        for i in range(self.numenemy):
        	r = rp()
        	self.enemylist.append(Enemy(self.corridor[r][0], self.corridor[r][1], 'v', 'virus'))
        r = rp()
        while (self.corridor[r][0], self.corridor[r][1]) == start:
        	r = rp()
        self.end = (self.corridor[r][0], self.corridor[r][1])
        self.skillcount = hero.skillcount
        r = rp()
        self.book = Book(book, self.corridor[r][0], self.corridor[r][1])
        r = rp()
        self.item = Item(item, self.corridor[r][0], self.corridor[r][1])


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
    return random.randint(21,69)

def randy(): 
    return random.randint(11, 34)

def randwalk(start):
	a = [start]
	current = start
	for i in range(3000):
		r = random.random()
		if r < 0.25:
			if current[0] < 68:
				current = (current[0] + 1, current[1])
		if 0.25 < r and r < 0.5:
			if current[0] > 21:
				current = (current[0] - 1, current[1])
		if r > 0.5 and r < 0.75:
			if current[1] < 33:
				current = (current[0], current[1] + 1)
		if r > 0.75:
			if current[1] > 11:
				current = (current[0], current[1] - 1)
		a.append(current)
	return a

def appendNewLevel(hero, dlvl, bookList, itemList, lvlList, messageList):
	b = random.randint(0,len(bookList)-1)
	if itemList:
		i = random.randint(0, len(itemList)-1)
	if random.random() < 0.2 and itemList:
		if dlvl % 2 == 0:
			lvlList.append(Level(hero.getpos(), dlvl, bookList[b], itemList[i], hero))
			if hero.glasses == 1:
				io.newMessage('You see ' + bookList[b], messageList)
			io.newMessage('You see ' + itemList[i], messageList)
			bookList.remove(bookList[b])
			itemList.remove(itemList[i])
		else:
			lvlList.append(Level(hero.getpos(), dlvl, bookList[b], 'none', hero))
			if hero.glasses == 1:
				io.newMessage('You see ' + bookList[b], messageList)
			bookList.remove(bookList[b])
	elif dlvl % 2 == 0 and itemList:
		lvlList.append(Level(hero.getpos(), dlvl, 'none',itemList[i], hero))
		io.newMessage('You see ' + itemList[i], messageList)
		itemList.remove(itemList[i])
	else:
		lvlList.append(Level(hero.getpos(), dlvl, 'none', 'none', hero))




