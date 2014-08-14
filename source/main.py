import pygcurse, pygame, sys, time, random, copy
from pygame.locals import *
from . import characters, level, io, pregame, book, item
from characters import Character as Character
from level import Level as Level
from io import Message as Message
from pregame import pregameLoop as pregameLoop

characters.Character = Character
io.Message = Message

#Main Window size and name

win = pygcurse.PygcurseWindow(70, 35)
win.font = pygame.font.SysFont('dejavuserif', 16, bold=False, italic=False)
pygame.display.set_caption('GradHack')
win.autowindowupdate = False
win.autoupdate = False

#Some auxilary functions and globals

messageList = []

bookList = ['Harry Potter', 'Lord of the Rings', 'Infinite Jest', 'Game of Thrones', 'Wheel of Time', 'Quantum Mechanics', 
    'Biochemistry', 'A Brief History of Time', 'Pharmacology', 'The Elements of Style']
itemList = ['coffee', 'tea', 'ramen noodles', 'laptop', 'beer', 'glasses', 'moleskin']

def attack(hero, opponent):
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 3
            io.newMessage("You've been hit. Lose 3 time.", messageList)
        else:
            opponent.health -= 1*(hero.strength)
            io.newMessage("You hit the virus.", messageList)



#Start the main pygame function

def main():

    newGame = False
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

    #Start the pregame (choose class, etc)
    
    startclass = pregame.pregameLoop(win)

    #Initialize some values

    dlvl = 0
    hero = Character(random.randint(21,69), random.randint(11, 34), '@', startclass)
    lvlList = []
    r = random.randint(0,len(itemList)-1)
    lvlList.append(Level(hero.getpos(), dlvl, 'none', itemList[r], hero))
    io.newMessage('You see ' + itemList[r], messageList)
    itemList.remove(itemList[r])
    level = lvlList[0]
    moveUp = moveDown = moveLeft = moveRight = False
    T = random.randint(1,3000)
    thesis = 0


    #Start the game loop
    t = 0
    while True:


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

        #Test for special skills

        if pressed == 48 and level.skillcount > 0:
            hero.useSkill(0, level)
            level.skillcount -= 1
            if hero.skills[0] == 'Banach-Tarski':
                io.newMessage("Banach-Tarski doubles the enemies!", messageList)

        if pressed == 49 and hero.lvl > 3 and level.skillcount > 0:
            hero.useSkill(1, level)
            level.skillcount -= 1
            if hero.skills[1] == 'Cryptography':
                io.newMessage("You encrypt your thesis to gain 3 time.", messageList)


        #Check for stairs to new level    
              
        if pressed == 46 and hero.getpos() == level.end:
            if dlvl < 9:
                dlvl += 1
            else:
                io.newMessage("You've reached the top floor.", messageList)
            if len(lvlList) == dlvl:
                b = random.randint(0,len(bookList)-1)
                i = random.randint(0, len(itemList)-1)
                if random.random() < 0.2:
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
                elif dlvl % 2 == 0:
                    lvlList.append(Level(hero.getpos(), dlvl, 'none',itemList[i], hero))
                    io.newMessage('You see ' + itemList[i], messageList)
                    itemList.remove(itemList[i])
                else:
                    lvlList.append(Level(hero.getpos(), dlvl, 'none', 'none', hero))
        if pressed == 46 and hero.getpos() == level.start:
            if dlvl > 0:
                dlvl -= 1
            else:
                io.newMessage("Cannot descend anymore.", messageList)

        #Check for books and items

        if pressed == 46 and hero.getpos() == level.book.getpos():
            book.usebook(level.book.name, messageList, hero, level, t)
            level.book.name = 'none'

        if pressed == 46 and hero.getpos() == level.item.getpos():
            i = copy.copy(level.item)
            hero.items.append(i)
            item.useitem(i.name, messageList, hero, level, t)
            level.item.name = 'none'

        #Check for thesis

        if dlvl == 9:
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

        
        #Attack system

        for enemy in level.enemylist:
            if moveUp and hero.getpos() == (enemy.posx,enemy.posy+1):
                attack(hero, enemy)
            elif moveDown and hero.getpos() == (enemy.posx,enemy.posy-1):
                attack(hero, enemy)
            elif moveLeft and hero.getpos() == (enemy.posx+1,enemy.posy):
                attack(hero, enemy)
            elif moveRight and hero.getpos() == (enemy.posx-1,enemy.posy):
                attack(hero, enemy)

        moveUp = moveDown = moveLeft = moveRight = False

        for enemy in level.enemylist:
            if enemy.health <= 0:
                level.enemylist.remove(enemy)
                io.newMessage('Enemy destroyed. Virus stalls rival by ' + str(hero.v) + '.', messageList)
                hero.time += hero.v
                if enemy.name == 'virus':
                    hero.xp += 5

        hero.checkLvl()
        hero.checkSkills()

        
        io.drawscreen(win, level, messageList, hero, thesis, dlvl, t, T)
        win.update()
        pygame.display.update()
        t += 1
        if t < hero.speedterminate:
            if t % hero.speed == 0:
                hero.time -= 1
        else:
            hero.time -= 1

        if newGame == True:
            main()

        
if __name__ == '__main__':
    main()