import pygcurse, pygame, sys, time, random
from pygame.locals import *
from . import characters, level, io
from characters import Character as Character
from level import Level as Level
from io import Message as Message

characters.Character = Character
io.Message = Message

#Main Window size and name
win = pygcurse.PygcurseWindow(60, 30)
pygame.display.set_caption('GradHack')
win.autowindowupdate = False
win.autoupdate = False

messageList = []

#Some simple auxilary functions

def legalspace(x,y, level):
    tmp1 = (x >= 10 and x < 60 and y >= 5 and y < 30)
    tmp2 = True
    for enemy in level.enemylist:
        tmp2 = (tmp2 and (x,y) != (enemy.posx, enemy.posy))
    return tmp1 and tmp2

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

    moveUp = moveDown = moveLeft = moveRight = False
    hero = Character(randx(), randy(), '@')
    level = Level(50, 25)

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

        win.fill('.', region = (10, 5, 50, 25), fgcolor='silver', bgcolor='olive')
        win.putchar(hero.c, hero.posx, hero.posy)
        for enemy in level.enemylist:
            win.putchar(enemy.c, enemy.posx, enemy.posy)
            if nearby(hero, enemy.posx, enemy.posy):
                win.write('Virus health: ' + str(enemy.health), 10, 1, fgcolor='white')
        win.write('HP: ' + str(hero.health) + '/5', 10, 0, fgcolor='white')
        win.write('Turn: ' + str(t), 0, 5, fgcolor='white')
        win.write('Items:', 0, 7, fgcolor='white')
        for message in messageList:
            if message.count == 4:
                win.write(message.message + ' '*10, 10, message.count, fgcolor='red')
            else:
                win.write(message.message + ' '*10, 10, message.count, fgcolor='green')

        win.update()
        pygame.display.update()
        t += 1
        
        #Test for the end of the game and break out if over

        if hero.health == 0:
            break

        if not level.enemylist:
            break

    #Display whether you won or lost    
        
    if hero.health == 0:
        win.write('You lose.', 10, 2, fgcolor='white')
        win.update()
        pygame.display.update()
        time.sleep(5)
        pygcurse.waitforkeypress()

    if enemy.health == 0:
        win.write('You win!', 10, 2, fgcolor='white')
        win.update()
        pygame.display.update()
        time.sleep(5)
        pygcurse.waitforkeypress()
  
        


if __name__ == '__main__':
    main()