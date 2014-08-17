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
        elif cl == 'lit':
            self.skills = ['Post-Modern']
        elif cl == 'music':
            self.skills = ['Sing']
        else:
            self.skills = ['None']

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
            elif self.cl == 'lit':
                if self.xp == 25:
                    self.skills.append('Epic Poem')
                if self.xp == 200:
                    self.skills.append('Deconstruction')
            elif self.cl == 'music':
                if self.xp == 25:
                    self.skills.append('Post-Tonal')
                if self.xp == 200:
                    self.skills.append('Neo-Riemannian')



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

def moveTowardHero(enemy, hero, level):
    x = 0
    y = 0
    if hero.posx - enemy.posx > 0:
        x = 2
    else:
        x = -2
    if hero.posy - enemy.posy > 0:
        y = 2
    else:
        y = -2
    if level.legalspace(enemy.posx + x, enemy.posy + y):
        enemy.posx += x
        enemy.posy += y

def moveAwayHero(enemy, hero, level):
    x = 0
    y = 0
    if hero.posx - enemy.posx > 0:
        x = -1
    else:
        x = 1
    if hero.posy - enemy.posy > 0:
        y = -1
    else:
        y = 1
    if level.legalspace(enemy.posx + x, enemy.posy + y):
        enemy.posx += x
        enemy.posy += y




