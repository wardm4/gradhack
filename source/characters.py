import random

#Character is for the main hero

xplevels = [10, 25, 45, 75, 120, 200, 310, 500, 750]

class Character(object):
    def __init__(self, posx, posy, c, cl):
        self.time = 150
        self.posx = posx
        self.posy = posy
        self.c = c
        self.cl = cl
        self.xp = 0
        self.lvl = 1
        self.items = []
        self.speed = 1
        self.speedterminate = 0
        self.v = 5
        self.strength = 1
        self.ne = 0
        if cl == 'math':
            self.skills = ['Banach-Tarski']
        if cl == 'lit':
            self.skills = ['Post-Modern']

    def getpos(self):
        return (self.posx, self.posy)

    def levelUpLoop(self, XP):
        for i in range(1,XP+1):
            self.xp += 1
            if self.xp in xplevels:
                self.lvl += 1
            if self.xp == 45:
                self.strength += 1
            if self.xp == 500:
                self.strength += 1
            if self.cl == 'math':
                if self.xp == 25:
                    self.skills.append('Cryptography')
                if self.xp == 200:
                    self.skills.append('Non-Euclidean')



    def useSkill(self, n, level):
        tmp = []
        if self.skills[n] == 'Banach-Tarski':
            for enemy in level.enemylist:
                tmp.append(enemy)
                r = random.randint(1,3000)
                tmp.append(Enemy(level.getx(r), level.gety(r), enemy.c, enemy.name))
            level.enemylist = tmp

        if self.skills[n] == 'Cryptography':
            self.time += 6

        if self.skills[n] == 'Non-Euclidean':
            self.ne = 1


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



