import random

#Character is for the main hero

class Character(object):
    def __init__(self, posx, posy, c, cl):
        self.time = 100
        self.posx = posx
        self.posy = posy
        self.c = c
        self.cl = cl
        self.xp = 0
        self.lvl = 1
        self.skills = []

    def getpos(self):
        return (self.posx, self.posy)

    def checkLvl(self):
        if self.xp >= 10:
            self.lvl = 2
        if self.xp >= 25:
            self.lvl = 3
        if self.xp >= 45:
            self.lvl = 4
        if self.xp >= 75:
            self.lvl = 5
        if self.xp >= 120:
            self.lvl = 6
        if self.xp >= 200:
            self.lvl = 7
        if self.xp >= 310:
            self.lvl = 8
        if self.xp >= 500:
            self.lvl

    def checkSkills(self):
        if self.cl == 'math':
            if self.lvl <= 3:
                self.skills = ['Banach-Tarski']
            if self.lvl > 3 and self.lvl <= 7:
                self.skills = ['Banach-Tarski', 'Nothing']

    def useSkill(self, n, level):
        tmp = []
        if self.skills[n] == 'Banach-Tarski':
            for enemy in level.enemylist:
                tmp.append(enemy)
                r = random.randint(1,3000)
                tmp.append(Enemy(level.getx(r), level.gety(r), enemy.c, enemy.name))
            level.enemylist = tmp


#Enemy keeps track of all other actors

class Enemy(object):
    def __init__(self, posx, posy, c, name):
        if name == 'virus':
            self.health = 2
        if name == 'student':
            self.health = 5
        self.posx = posx
        self.posy = posy
        self.c = c
        self.name = name

    def name(self):
        return self.name

    def getpos(self):
        return (self.posx, self.posy)



