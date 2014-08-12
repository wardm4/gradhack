import pygcurse, pygame

def nearby(a, x, y):
    if abs(a.posx - x) < 3 and abs(a.posy - y) < 3:
        return True
    else:
        return False

#Basic input/output structures

class Message(object):
    def __init__(self, message):
        self.count = 4
        self.message = message

def newMessage(s, messageList):
    for mess in messageList:
        mess.count -= 1
        if mess.count < 2:
            messageList.remove(mess)
    messageList.append(Message(s))



# Display the "dungeon" and character info, and message queue.

def drawscreen(win, level, messageList, hero, thesis, dlvl, t):
    win.fill(' ', region = (0, 0, 60, 30), fgcolor='black', bgcolor='black')
    win.fill('.', region = (10, 5, 50, 25), fgcolor='silver', bgcolor='olive')
    for space in level.corridor:
        win.putchar('.', space[0], space[1], fgcolor='silver', bgcolor='black')

    for enemy in level.enemylist:
        win.putchar(enemy.c, enemy.posx, enemy.posy, fgcolor='red', bgcolor='black')
        if nearby(hero, enemy.posx, enemy.posy):
            win.write('Virus health: ' + str(enemy.health), 10, 1, fgcolor='white')

    win.putchar('>', level.start[0], level.start[1], fgcolor='fuchsia', bgcolor='black')
    win.putchar('<', level.end[0], level.end[1], fgcolor='fuchsia', bgcolor='black')
    if thesis == 0 and dlvl == 5:
        win.putchar('T', level.getx(T), level.gety(T), fgcolor='fuchsia')
    win.putchar(hero.c, hero.posx, hero.posy)
    

    win.write('HP: ' + str(hero.health) + '/5', 10, 0, fgcolor='white')
    win.write('Turn: ' + str(t), 0, 5, fgcolor='white')
    win.write('DLvl: ' + str(dlvl + 1), 0, 6, fgcolor='white')
    win.write('Items:', 0, 7, fgcolor='white')
    if thesis == 1:
        win.write('Thesis', 0, 8, fgcolor='yellow')

    for message in messageList:
        if message.count == 4:
            win.write(message.message + ' '*10, 10, message.count, fgcolor='red')
        else:
            win.write(message.message + ' '*10, 10, message.count, fgcolor='green')

    if dlvl == 0 and thesis == 1 and hero.getpos() == level.start:
        newMessage("Congratulations! You win!")

        

        win.update()
        pygame.display.update()