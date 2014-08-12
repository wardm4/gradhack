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

#Start the main pygame function

def main():

    #Initialize some values
    hero = Character(random.randint(11,59), random.randint(6, 29), '@')
    lvlList = []
    lvlList.append(Level(hero.getpos()))
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
              
        if pressed == 46 and hero.getpos() == level.end:
            if len(lvlList) - 1 == dlvl:
                lvlList.append(Level(hero.getpos()))
            if dlvl < 5:
                dlvl += 1
            else:
                io.newMessage("You've reached the top floor.", messageList)
        if pressed == 46 and hero.getpos() == level.start:
            if dlvl > 0:
                dlvl -= 1
            else:
                io.newMessage("Cannot descend anymore.", messageList)

        #Check for thesis

        if dlvl == 5:
            if pressed == 46 and hero.getpos() == (level.getx(T), level.gety(T)):
                io.newMessage("You've got your thesis back!", messageList)
                thesis = 1


        level = lvlList[dlvl]
        

        # move the player (if allowed)
        
        if moveUp and level.legalspace(hero.posx, hero.posy-1):
            hero.posy -= 1
        if moveDown and level.legalspace(hero.posx, hero.posy+1):
            hero.posy += 1
        if moveLeft and level.legalspace(hero.posx-1, hero.posy):
            hero.posx -= 1
        if moveRight and level.legalspace(hero.posx+1, hero.posy):
            hero.posx += 1

        att = 0
        #A very basic 50/50 attack system
        for enemy in level.enemylist:
            if moveUp and hero.getpos() == (enemy.posx,enemy.posy+1):
                hero.attack(enemy)
                att = 1
            elif moveDown and hero.getpos() == (enemy.posx,enemy.posy-1):
                hero.attack(enemy)
                att = 1
            elif moveLeft and hero.getpos() == (enemy.posx+1,enemy.posy):
                hero.attack(enemy)
                att = 1
            elif moveRight and hero.getpos() == (enemy.posx-1,enemy.posy):
                hero.attack(enemy)
                att = 1

        if att == 1:
            io.newMessage('You attack.', messageList)
            

        if (hero.health < 5) and (random.random() > 0.8) and (att == 0):
            hero.health += 1

        
        moveUp = moveDown = moveLeft = moveRight = False

        for enemy in level.enemylist:
            if enemy.health == 0:
                level.enemylist.remove(enemy)
                io.newMessage('Enemy destroyed.', messageList)

        
        io.drawscreen(win, level, messageList, hero, thesis, dlvl, t)
        win.update()
        pygame.display.update()
        t += 1

        
if __name__ == '__main__':
    main()