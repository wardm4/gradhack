import pygcurse, pygame

def nearby(a, x, y):
    if abs(a.posx - x) < 3 and abs(a.posy - y) < 3:
        return True
    else:
        return False

#Basic input/output structures

class Message(object):
    def __init__(self, message):
        self.count = 9
        self.message = message

def newMessage(s, messageList):
    for mess in messageList:
        mess.count -= 1
        if mess.count < 1:
            messageList.remove(mess)
    messageList.append(Message(s))



# Display the "dungeon" and character info, and message queue.

def drawscreen(win, level, messageList, hero, thesis, dlvl, t, T):

	#Draw the level and enemies

    win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
    win.fill('.', region = (20, 10, 50, 25), fgcolor='silver', bgcolor='olive')
    for space in level.corridor:
        win.putchar('.', space[0], space[1], fgcolor='silver', bgcolor='black')

    for enemy in level.enemylist:
        win.putchar(enemy.c, enemy.posx, enemy.posy, fgcolor='red', bgcolor='black')
        if nearby(hero, enemy.posx, enemy.posy):
            win.write('Virus health: ' + str(enemy.health), 20, 0, fgcolor='white')

    #Draw individual characters on level

    win.putchar('>', level.start[0], level.start[1], fgcolor='fuchsia', bgcolor='black')
    win.putchar('<', level.end[0], level.end[1], fgcolor='fuchsia', bgcolor='black')
    if level.book.name != 'none':
    	win.putchar('~', level.book.posx, level.book.posy, fgcolor='yellow', bgcolor='black')
    if level.item.name != 'none':
    	win.putchar('!', level.item.posx, level.item.posy, fgcolor='yellow', bgcolor='black')
    if thesis == 0 and dlvl == 9:
        win.putchar('T', level.getx(T), level.gety(T), fgcolor='fuchsia')
    win.putchar(hero.c, hero.posx, hero.posy)

    #Draw stats

    win.write('Time\n ' + str(hero.time), 1, 1, fgcolor='red')
    win.write('Turn: ' + str(t), 0, 10, fgcolor='white')
    win.write('Lvl: ' + str(hero.lvl), 0, 11, fgcolor='white')
    
    #Draw things visible only with moleskin

    if "moleskin" in hero.items:
    	win.write('XP: ' + str(hero.xp), 0, 12, fgcolor='white')
    	win.write('Floor: ' + str(dlvl + 1), 0, 13, fgcolor='white')
    	win.write('Strength: ' + str(hero.strength), 0, 29, fgcolor='white')
    	win.write('Speed: ' + str(hero.speed), 0, 30, fgcolor='white')
    	win.write('Viruses stall: ' + str(hero.v), 0, 31, fgcolor='white')

    win.write('Skills: ' + str(level.skillcount), 0, 15, fgcolor='white')
    for i in range(len(hero.skills)):
    	win.write(str(i) + '.' + hero.skills[i], 0, 16 + i, fgcolor='yellow')
    win.write('Items:', 0, 20, fgcolor='white')
    if thesis == 1:
        win.write('Thesis', 0, 21, fgcolor='fuchsia')
    for i in range(len(hero.items)):
    	if hero.items[i] != 'none':
    		win.write(hero.items[i], 0, 22 + i, fgcolor='yellow')

    for message in messageList:
        if message.count == 9:
            win.write(message.message, 20, message.count, fgcolor='red')
        else:
            win.write(message.message, 20, message.count, fgcolor='green')

    if dlvl == 0 and thesis == 1 and hero.getpos() == level.start:
        newMessage("Congratulations! You win!", messageList)

        
