import pygcurse, pygame, sys, time, random
from pygame.locals import *
from . import characters, level, io, pregame
from characters import Character as Character
from level import Level as Level
from io import Message as Message
from pregame import pregameLoop as pregameLoop

characters.Character = Character
io.Message = Message

#Main Window size and name
win = pygcurse.PygcurseWindow(60, 30)
pygame.display.set_caption('GradHack')
win.autowindowupdate = False
win.autoupdate = False

#Some simple auxilary functions

messageList = []

def legalspace(x,y, level):
    tmp2 = True
    for enemy in level.enemylist:
        tmp2 = (tmp2 and (x,y) != (enemy.posx, enemy.posy))
    return tmp2 and (x,y) in level.corridor

def randx():
    return random.randint(11,59)

def randy(): 
    return random.randint(6, 29)

def nearby(a, x, y):
    if abs(a.posx - x) < 3 and abs(a.posy - y) < 3:
        return True
    else:
        return False

def newMessage(message):
    for mess in messageList:
        mess.count -= 1
        if mess.count < 2:
            messageList.remove(mess)
    messageList.append(Message(message))
 
#Start the main pygame function

def main():

    #Initialize some values
    hero = Character(randx(), randy(), '@')
    lvlList = []
    lvlList.append(Level((hero.posx, hero.posy)))
    dlvl = 0
    level = lvlList[0]
    moveUp = moveDown = moveLeft = moveRight = False
    T = random.randint(1,3000)
    thesis = 0

    #Start the pregame (choose class, etc)
    
    pregame.pregameLoop(win)


    #Start the game loop
    t = 0
    while True:

        pygame.event.set_allowed(None)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        e = pygame.event.wait()
        pressed = e.key

        
        #Get input with standard vi keybinding or arrow keys

        if pressed == 8:
            newGame = True
        elif pressed == 27:
            pygame.quit()
            sys.exit()
        elif pressed == 273 or pressed == 107:
            moveUp = True
        elif pressed == 274 or pressed == 106:
            moveDown = True
        elif pressed == 276 or pressed == 104:
            moveLeft = True
        elif pressed == 275 or pressed == 108:
            moveRight = True
        elif pressed == 117:
            moveRight = True
            moveUp = True
        elif pressed == 121:
            moveLeft = True
            moveUp = True
        elif pressed == 110:
            moveRight = True
            moveDown = True
        elif pressed == 98:
            moveLeft = True
            moveDown = True

        #Check for stairs to new level    
              
        if pressed == 46 and (hero.posx, hero.posy) == level.end:
            if len(lvlList) - 1 == dlvl:
                lvlList.append(Level((hero.posx, hero.posy)))
            if dlvl < 5:
                dlvl += 1
            else:
                newMessage("You've reached the top floor.")
        if pressed == 46 and (hero.posx, hero.posy) == level.start:
            if dlvl > 0:
                dlvl -= 1
            else:
                newMessage("Cannot descend anymore.")

        #Check for thesis

        if dlvl == 5:
            if pressed == 46 and (hero.posx, hero.posy) == (level.corridor[T][0], level.corridor[T][1]):
                newMessage("You've got your thesis back!")
                thesis = 1


        level = lvlList[dlvl]
        

        # move the player (if allowed)
        
        if moveUp and legalspace(hero.posx, hero.posy-1, level):
            hero.posy -= 1
        if moveDown and legalspace(hero.posx, hero.posy+1, level):
            hero.posy += 1
        if moveLeft and legalspace(hero.posx-1, hero.posy, level):
            hero.posx -= 1
        if moveRight and legalspace(hero.posx+1, hero.posy, level):
            hero.posx += 1

        att = 0
        #A very basic 50/50 attack system
        for enemy in level.enemylist:
            if moveUp and (hero.posx, hero.posy) == (enemy.posx,enemy.posy+1):
                hero.attack(enemy)
                att = 1
            elif moveDown and (hero.posx, hero.posy) == (enemy.posx,enemy.posy-1):
                hero.attack(enemy)
                att = 1
            elif moveLeft and (hero.posx, hero.posy) == (enemy.posx+1,enemy.posy):
                hero.attack(enemy)
                att = 1
            elif moveRight and (hero.posx, hero.posy) == (enemy.posx-1,enemy.posy):
                hero.attack(enemy)
                att = 1

        if att == 1:
            newMessage('You attack.')
            

        if (hero.health < 5) and (random.random() > 0.8) and (att == 0):
            hero.health += 1

        
        moveUp = moveDown = moveLeft = moveRight = False

        for enemy in level.enemylist:
            if enemy.health == 0:
                level.enemylist.remove(enemy)
                newMessage('Enemy destroyed.')

        # Display the "dungeon" and character info, and message queue.
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
            win.putchar('T', level.corridor[T][0], level.corridor[T][1], fgcolor='fuchsia')
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

        if dlvl == 0 and thesis == 1 and (hero.posx, hero.posy) == level.start:
            newMessage("Congratulations! You win!")

        

        win.update()
        pygame.display.update()
        t += 1

        
        



        


if __name__ == '__main__':
    main()