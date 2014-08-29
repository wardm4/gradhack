import random
import characters as ch
import book as bk
import item as itm
import io

# Random placement function


def rp():
    return random.randint(1, 3000)


class Level(object):
    def __init__(self, start, dlvl, book, item, skillcount):
        self.xsize = 50
        self.ysize = 25
        self.start = start
        self.corridor = randwalk(start)
        r = rp()
        while self.corridor[r] == start:
            r = rp()
        self.end = self.corridor[r]
        numvirus = random.randint(1, 5)
        numstudent = random.randint(1, 5)
        numinternets = random.randint(1, 5)
        self.enemylist = []
        for i in range(numvirus):
            r = rp()
            while self.corridor[r] == self.end:
                r = rp()
            self.enemylist.append(ch.Enemy(self.getx(r), self.gety(r), 'v', 'Virus'))
        if dlvl >= 2:
            for i in range(numstudent):
                r = rp()
                while (self.getx(r), self.gety(r)) == self.end:
                    r = rp()
                self.enemylist.append(ch.Enemy(self.getx(r), self.gety(r), 's', 'Student'))
        if dlvl >= 5:
            for i in range(numinternets):
                r = rp()
                while self.corridor[r] == self.end:
                    r = rp()
                self.enemylist.append(ch.Enemy(self.getx(r), self.gety(r), 'I', 'Internet Monster'))
        if dlvl >= 8:
            if random.random() <= 0.3:
                r = rp()
                self.enemylist.append(ch.Enemy(self.getx(r), self.gety(r), 'c', 'Committee Member'))
        self.skillcount = skillcount
        r = rp()
        self.book = bk.Book(book, self.getx(r), self.gety(r))
        r = rp()
        self.item = itm.Item(item, self.getx(r), self.gety(r))

    def getx(self, n):
        return self.corridor[n][0]

    def gety(self, n):
        return self.corridor[n][1]

    def startx(self):
        return self.start[0]

    def starty(self):
        return self.start[1]

    def endx(self):
        return self.end[0]

    def endy(self):
        return self.end[1]

    def legalspace(self, x, y):
        tmp2 = True
        for enemy in self.enemylist:
            tmp2 = (tmp2 and (x, y) != enemy.getpos())
        return tmp2 and (x, y) in self.corridor

# Functions for making levels


def randx():
    return random.randint(21, 69)


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


def makenewlevel(hero, dlvl, bookList, itemList, lvlList, messageList, skillcount):
    b = random.randint(0, len(bookList) - 1)
    if itemList:
        i = random.randint(0, len(itemList) - 1)
    if random.random() < 0.2 and itemList:
        if dlvl % 2 == 0:
            return Level(hero.getpos(), dlvl, bookList[b], itemList[i], skillcount)
        else:
            return Level(hero.getpos(), dlvl, bookList[b], 'none', skillcount)
    elif dlvl % 2 == 0 and itemList:
        return Level(hero.getpos(), dlvl, 'none', itemList[i], skillcount)
    else:
        return Level(hero.getpos(), dlvl, 'none', 'none', skillcount)
