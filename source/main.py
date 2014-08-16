import pygcurse, pygame, sys, time, random, copy
from pygame.locals import *
from . import characters, level, io, pregame, book, item, endgame
from characters import Character
from level import Level
from io import Message
from pregame import pregameLoop
from endgame import winloop, loseloop

characters.Character = Character
io.Message = Message

#Main Window size and name

win = pygcurse.PygcurseWindow(70, 35)
win.font = pygame.font.SysFont('dejavuserif', 16, bold=False, italic=False)
pygame.display.set_caption('GradHack')
win.autowindowupdate = False
win.autoupdate = False

#Some auxilary functions and globals

def attack(hero, opponent, messageList):
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 3
            io.newMessage("You've been hit. Lose 3 time.", messageList)
        else:
            opponent.health -= 1*(hero.strength)
            io.newMessage("You hit the virus.", messageList)

def neDist():
    r = random.random()
    if r < 0.7:
        return 0
    elif r < 0.9:
        return 1
    else:
        return 2



#Start the main pygame function

def main():

    newGame = False
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

    #Start the pregame (choose class, etc)
    
    startclass = pregame.pregameLoop(win)

    #Initialize some values

    messageList = []
    bookList = ['Harry Potter', 'Lord of the Rings', 'Infinite Jest', 'Game of Thrones', 'Wheel of Time', 'Quantum Mechanics', 
        'Biochemistry', 'A Brief History of Time', 'Pharmacology', 'The Elements of Style']
    itemList = ['coffee', 'tea', 'ramen noodles', 'laptop', 'beer', 'glasses', 'moleskin']

    dlvl = 0
    hero = Character(random.randint(21,69), random.randint(11, 34), '@', startclass)
    lvlList = []
    r = random.randint(0,len(itemList)-1)
    lvlList.append(Level(hero.getpos(), dlvl, 'none', itemList[r], hero))
    io.newMessage('You see ' + itemList[r], messageList)
    itemList.remove(itemList[r])
    lvl = lvlList[0]
    moveUp = moveDown = moveLeft = moveRight = False
    T = random.randint(1,3000)
    thesis = 0
    XP = 0


    #Start the game loop
    t = 0
    while True:


        e = pygame.event.wait()
        pressed = e.key

        
        #Move with vi keybinding or arrow keys

        if pressed == 8:
            newGame = True
        elif pressed == 27:
            pygame.quit()
            sys.exit()
        elif (pressed == 273 or pressed == 107):
            if lvl.legalspace(hero.posx, hero.posy-1):
                hero.posy -= 1
            moveUp = True
        elif (pressed == 274 or pressed == 106):
            if lvl.legalspace(hero.posx, hero.posy+1):
                hero.posy += 1
            moveDown = True
        elif (pressed == 276 or pressed == 104):
            if lvl.legalspace(hero.posx-1, hero.posy):
                hero.posx -= 1
            moveLeft = True
        elif (pressed == 275 or pressed == 108):
            if lvl.legalspace(hero.posx+1, hero.posy):
                hero.posx += 1
            moveRight = True
        elif pressed == 117:
            if lvl.legalspace(hero.posx+1, hero.posy-1):
                hero.posx += 1
                hero.posy -= 1
            moveRight = True
            moveUp = True
        elif pressed == 121:
            if lvl.legalspace(hero.posx-1, hero.posy-1):
                hero.posx -= 1
                hero.posy -= 1
            moveLeft = True
            moveUp = True
        elif pressed == 110:
            if lvl.legalspace(hero.posx+1, hero.posy+1):
                hero.posx += 1
                hero.posy += 1
            moveRight = True
            moveDown = True
        elif pressed == 98:
            if lvl.legalspace(hero.posx-1, hero.posy+1):
                hero.posx -= 1
                hero.posy += 1
            moveLeft = True
            moveDown = True


        #Test for special skills

        if pressed == 48 and lvl.skillcount > 0:
            hero.useSkill(0, lvl)
            lvl.skillcount -= 1
            if hero.skills[0] == 'Banach-Tarski':
                io.newMessage("Banach-Tarski doubles the enemies!", messageList)
            if hero.skills[0] == 'Post-Modern':
                io.newMessage("Post-Modern analysis.", messageList)
                io.newMessage("Nothing is what it seems.", messageList)
                level.appendNewLevel(hero, dlvl, bookList, itemList, lvlList, messageList)

        if pressed == 49 and hero.lvl > 3 and lvl.skillcount > 0:
            hero.useSkill(1, lvl)
            lvl.skillcount -= 1
            if hero.skills[1] == 'Cryptography':
                io.newMessage("You encrypt your thesis to gain 3 time.", messageList)

        if pressed == 50 and hero.lvl >= 7 and lvl.skillcount > 0:
            hero.useSkill(2, lvl)
            lvl.skillcount -= 1
            if hero.skills[2] == 'Non-Euclidean':
                io.newMessage("World is now Non-Euclidean.", messageList)
                io.newMessage("Distance is unpredictable.", messageList)


        #Check for stairs to new lvl    
              
        if pressed == 46 and hero.getpos() == lvl.end:
            if dlvl < 9:
                dlvl += 1
            else:
                io.newMessage("You've reached the top floor.", messageList)
            if len(lvlList) == dlvl:
                level.appendNewLevel(hero, dlvl, bookList, itemList, lvlList, messageList)
        if pressed == 46 and hero.getpos() == lvl.start:
            if dlvl > 0:
                dlvl -= 1
            else:
                io.newMessage("Cannot descend anymore.", messageList)

        #Check for books and items

        if pressed == 46 and hero.getpos() == lvl.book.getpos():
            XP += book.usebook(lvl.book.name, messageList, hero, lvl, t)
            lvl.book.name = 'none'

        if pressed == 46 and hero.getpos() == lvl.item.getpos():
            i = copy.copy(lvl.item)
            hero.items.append(i)
            XP += item.useitem(i.name, messageList, hero, lvl, t)
            lvl.item.name = 'none'

        #Check for thesis

        if dlvl == 9:
            if pressed == 46 and hero.getpos() == (lvl.getx(T), lvl.gety(T)):
                io.newMessage("You've got your thesis back!", messageList)
                thesis = 1


        lvl = lvlList[dlvl]

        
        #Attack system

        for enemy in lvl.enemylist:
            if moveUp and hero.getpos() == (enemy.posx,enemy.posy+1):
                attack(hero, enemy, messageList)
            elif moveDown and hero.getpos() == (enemy.posx,enemy.posy-1):
                attack(hero, enemy, messageList)
            elif moveLeft and hero.getpos() == (enemy.posx+1,enemy.posy):
                attack(hero, enemy, messageList)
            elif moveRight and hero.getpos() == (enemy.posx-1,enemy.posy):
                attack(hero, enemy, messageList)

        moveUp = moveDown = moveLeft = moveRight = False

        for enemy in lvl.enemylist:
            if enemy.health <= 0:
                lvl.enemylist.remove(enemy)
                io.newMessage('Enemy destroyed. Virus stalls rival by ' + str(hero.v) + '.', messageList)
                hero.time += hero.v
                if enemy.name == 'virus':
                    XP += 5

        hero.levelUpLoop(XP)
        XP = 0
        
        io.drawscreen(win, lvl, messageList, hero, thesis, dlvl, t, T)
        win.update()
        pygame.display.update()
        t += 1
        if t < hero.speedterminate:
            if t % hero.speed == 0:
                hero.time -= 1
        #ne = non-euclidean
        elif hero.ne == 1:
            hero.time -= neDist()
        else:
            hero.time -= 1

        if newGame == True:
            main()

        # Win/Lose

        if dlvl == 0 and pressed == 46 and hero.getpos() == lvl.start and thesis == 1:
            endgame.winloop(win)
            main()
        if hero.time < 0:
            endgame.loseloop(win)
            main()

        
if __name__ == '__main__':
    main()