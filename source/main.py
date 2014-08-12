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

def attack(hero, opponent):
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 5
            io.newMessage("You've been hit. Lose 5 time.", messageList)
        else:
            opponent.health -= 1
            io.newMessage("You hit the virus.", messageList)

#Start the main pygame function

def main():

    

    #Start the pregame (choose class, etc)
    
    startclass = pregame.pregameLoop(win)

    #Initialize some values
    dlvl = 0
    hero = Character(random.randint(11,59), random.randint(6, 29), '@', startclass)
    lvlList = []
    lvlList.append(Level(hero.getpos(), dlvl))
    level = lvlList[0]
    moveUp = moveDown = moveLeft = moveRight = False
    T = random.randint(1,3000)
    thesis = 0


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

        if pressed == 48:
            hero.useSkill(0, level)
            if hero.skills[0] == 'B-T':
                io.newMessage("Banach-Tarski doubles the enemies!", messageList)


        #Check for stairs to new level    
              
        if pressed == 46 and hero.getpos() == level.end:
            if dlvl < 5:
                dlvl += 1
            else:
                io.newMessage("You've reached the top floor.", messageList)
            if len(lvlList) == dlvl:
                lvlList.append(Level(hero.getpos(), dlvl))
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
                attack(hero, enemy)
                att = 1
            elif moveDown and hero.getpos() == (enemy.posx,enemy.posy-1):
                attack(hero, enemy)
                att = 1
            elif moveLeft and hero.getpos() == (enemy.posx+1,enemy.posy):
                attack(hero, enemy)
                att = 1
            elif moveRight and hero.getpos() == (enemy.posx-1,enemy.posy):
                attack(hero, enemy)
                att = 1

        moveUp = moveDown = moveLeft = moveRight = False

        for enemy in level.enemylist:
            if enemy.health == 0:
                level.enemylist.remove(enemy)
                io.newMessage('Enemy destroyed. Virus stalls rival by 5.', messageList)
                hero.time += 5
                if enemy.name == 'virus':
                    hero.xp += 5

        hero.checkLvl()
        hero.checkSkills()

        
        io.drawscreen(win, level, messageList, hero, thesis, dlvl, t, T)
        win.update()
        pygame.display.update()
        t += 1
        hero.time -= 1

        
if __name__ == '__main__':
    main()