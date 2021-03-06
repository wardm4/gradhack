import pygcurse
import pygame
import sys
import random
import copy
import io
import level
import book
import item
import endgame
import characters as ch
import pregame
from level import Level

# Main Window size and name

win = pygcurse.PygcurseWindow(70, 35)
win.font = pygame.font.SysFont('dejavuserif', 16, bold=False, italic=False)
pygame.display.set_caption('GradHack')
win.autowindowupdate = False
win.autoupdate = False

# Some auxilary functions and globals


def attack(hero, opponent, messageList):
    if opponent.name == 'Virus':
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 3
            io.new_message("Virus evades you. Lose 3 time.", messageList)
        else:
            opponent.health -= hero.strength
            io.new_message("You hit the virus.", messageList)
    if opponent.name == 'Student':
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 3
            io.new_message("Student annoys you. Lose 3 time.", messageList)
        else:
            opponent.health -= hero.strength
            io.new_message("You answer student questions.", messageList)
    if opponent.c == 'I':
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 5
            io.new_message("The internet distracts you. Lose 5 time.", messageList)
        else:
            opponent.health -= hero.strength
            io.new_message("You close a browser window.", messageList)
    if opponent.c == 'c':
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 5
            io.new_message("Committee member asks you about your thesis.", messageList)
        else:
            opponent.health -= hero.strength
            io.new_message("You successfully answer the question.", messageList)
    if opponent.c == 'R':
        if random.random() < (0.5 - 0.05 * (hero.lvl)):
            hero.time -= 10
            io.new_message("Rival hits you.", messageList)
        else:
            opponent.health -= hero.strength
            io.new_message("You hit your rival.", messageList)


def nedist():
    r = random.random()
    if r < 0.7:
        return 0
    elif r < 0.9:
        return 1
    else:
        return 2

# Start the main pygame function


def main():

    newGame = False
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

    # Start the pregame (choose class, etc)

    startclass = pregame.pregameLoop(win)

    # Initialize some values

    messageList = []
    bookList = ['Harry Potter', 'Lord of the Rings', 'Infinite Jest',
                'Game of Thrones', 'Wheel of Time', 'Quantum Mechanics',
                'Biochemistry', 'A Brief History of Time', 'Pharmacology',
                'The Elements of Style']
    itemList = ['coffee', 'tea', 'ramen noodles',
                'laptop', 'beer', 'glasses', 'moleskin']
    dlvl = 0
    hero = ch.Character(random.randint(21, 69), random.randint(11, 34), '@', startclass)
    lvlList = []
    r = random.randint(0, len(itemList) - 1)
    lvlList.append(Level(hero.getpos(), dlvl, 'none', itemList[r], 3))
    lvl = lvlList[0]
    moveUp = moveDown = moveLeft = moveRight = False
    T = random.randint(1, 3000)
    thesis = 0
    XP = 0
    rival = ch.Enemy(0, 0, 'R', 'Rival')

    # Start the game loop

    t = 0
    while True:

        e = pygame.event.wait()
        pressed = e.key
        attemptPos = (0, 0)

        # Move with vi keybinding or arrow keys

        if pressed == 8:
            newGame = True
        elif pressed == 27:
            pygame.quit()
            sys.exit()
        elif (pressed == 273 or pressed == 107):
            attemptPos = (hero.posx, hero.posy - 1)
            if lvl.legalspace(hero.posx, hero.posy - 1):
                hero.posy -= 1
        elif (pressed == 274 or pressed == 106):
            attemptPos = (hero.posx, hero.posy + 1)
            if lvl.legalspace(hero.posx, hero.posy + 1):
                hero.posy += 1
        elif (pressed == 276 or pressed == 104):
            attemptPos = (hero.posx - 1, hero.posy)
            if lvl.legalspace(hero.posx - 1, hero.posy):
                hero.posx -= 1
        elif (pressed == 275 or pressed == 108):
            attemptPos = (hero.posx + 1, hero.posy)
            if lvl.legalspace(hero.posx + 1, hero.posy):
                hero.posx += 1
        elif pressed == 117:
            attemptPos = (hero.posx + 1, hero.posy - 1)
            if lvl.legalspace(hero.posx + 1, hero.posy - 1):
                hero.posx += 1
                hero.posy -= 1
        elif pressed == 121:
            attemptPos = (hero.posx - 1, hero.posy - 1)
            if lvl.legalspace(hero.posx - 1, hero.posy - 1):
                hero.posx -= 1
                hero.posy -= 1
        elif pressed == 110:
            attemptPos = (hero.posx + 1, hero.posy + 1)
            if lvl.legalspace(hero.posx + 1, hero.posy + 1):
                hero.posx += 1
                hero.posy += 1
        elif pressed == 98:
            attemptPos = (hero.posx - 1, hero.posy + 1)
            if lvl.legalspace(hero.posx - 1, hero.posy + 1):
                hero.posx -= 1
                hero.posy += 1

        # Test for special skills

        if pressed == 48 and lvl.skillcount > 0:
            hero.useskill(0, lvl)
            lvl.skillcount -= 1
            if hero.skills[0] == 'Banach-Tarski':
                io.new_message("Banach-Tarski doubles the enemies!", messageList)
            elif hero.skills[0] == 'Post-Modern':
                io.new_message("Post-Modern analysis.", messageList)
                io.new_message("Nothing is what it seems.", messageList)
                lvlList[dlvl] = level.makenewlevel(
                    hero, dlvl, bookList, itemList, lvlList, messageList,
                    lvl.skillcount)
            elif hero.skills[0] == 'Sing':
                io.new_message("You sing.", messageList)
                io.new_message("Your song entrances the monsters.", messageList)
                for enemy in lvl.enemylist:
                    ch.movetohero(enemy, hero, lvl)

        if pressed == 49 and hero.lvl >= 3 and lvl.skillcount > 0:
            hero.useskill(1, lvl)
            lvl.skillcount -= 1
            if hero.skills[1] == 'Cryptography':
                io.new_message("You encrypt your thesis to gain 8 time.", messageList)
            elif hero.skills[1] == 'Epic Poem':
                io.new_message("You read an epic poem.", messageList)
                io.new_message("The monsters are entranced by it.", messageList)
                for enemy in lvl.enemylist:
                    ch.movetohero(enemy, hero, lvl)
            elif hero.skills[1] == 'Post-Tonal':
                io.new_message("Your post-tonal piece repels the monsters.", messageList)
                for enemy in lvl.enemylist:
                    ch.movefromhero(enemy, hero, lvl)

        if pressed == 50 and hero.lvl >= 7 and lvl.skillcount > 0:
            hero.useskill(2, lvl)
            lvl.skillcount -= 1
            if hero.skills[2] == 'Non-Euclidean':
                io.new_message("World is now Non-Euclidean.", messageList)
                io.new_message("Distance is unpredictable.", messageList)
            elif hero.skills[2] == 'Deconstruction':
                io.new_message("You deconstruct with differance.", messageList)
                for enemy in lvl.enemylist:
                    enemy.health -= hero.strength
            elif hero.skills[2] == 'Neo-Riemannian':
                io.new_message("Neo-Riemannian transformation applied.", messageList)
                lvlList[dlvl] = level.makenewlevel(
                    hero, dlvl, bookList, itemList, lvlList, messageList,
                    lvl.skillcount)

        # Check for stairs to new lvl

        if pressed == 46 and hero.getpos() == lvl.end:
            if dlvl < 9:
                dlvl += 1
            else:
                io.new_message("You've reached the top floor.", messageList)
            if len(lvlList) == dlvl:
                if "tea" in hero.items:
                    skillcount = 5
                else:
                    skillcount = 3
                lvlList.append(level.makenewlevel(
                    hero, dlvl, bookList, itemList, lvlList, messageList,
                    skillcount))
            hero.posx = lvlList[dlvl].startx()
            hero.posy = lvlList[dlvl].starty()
        if pressed == 46 and hero.getpos() == lvl.start:
            if dlvl > 0:
                dlvl -= 1
                hero.posx = lvlList[dlvl].endx()
                hero.posy = lvlList[dlvl].endy()
            else:
                io.new_message("Cannot descend anymore.", messageList)

        lvl = lvlList[dlvl]

        # Check for books and items

        if pressed == 46 and hero.getpos() == lvl.book.getpos():
            XP += book.usebook(lvl.book.name, messageList, hero, lvl, t)
            if lvl.book.name != 'none':
                bookList.remove(lvl.book.name)
            lvl.book.name = 'none'

        if pressed == 46 and hero.getpos() == lvl.item.getpos():
            i = copy.copy(lvl.item)
            hero.items.append(i.name)
            XP += item.useitem(i.name, messageList, hero, lvl, t)
            if i.name != 'none':
                itemList.remove(i.name)
            lvl.item.name = 'none'

        # Display items and books

        if dlvl == 9:
            if pressed == 46 and hero.getpos() == (lvl.getx(T), lvl.gety(T)):
                io.new_message("You've got your thesis back!", messageList)
                thesis = 1

        if hero.getpos() == lvl.start:
            if lvl.item.name != 'none':
                io.new_message('You see ' + lvl.item.name, messageList)
            if 'glasses' in hero.items:
                if lvl.book.name != 'none':
                    io.new_message('You see ' + lvl.book.name, messageList)

        # Update enemy status

        for enemy in lvl.enemylist:
            if attemptPos == enemy.getpos():
                attack(hero, enemy, messageList)
            ch.ai(enemy, hero, lvl)
            if enemy.health <= 0:
                lvl.enemylist.remove(enemy)
                if enemy.name == 'Virus':
                    XP += 5
                    io.new_message('Enemy destroyed. Virus stalls rival by '
                                   + str(hero.v) + '.', messageList)
                    hero.time += hero.v
                if enemy.name == 'Student':
                    XP += 10
                    io.new_message('Student leaves you alone.', messageList)
                if enemy.c == 'I':
                    XP += 20
                    io.new_message('You send cat videos to your rival.', messageList)
                    hero.time += 10
                if enemy.c == 'c':
                    XP += 30
                    io.new_message('Committee member goes to a meeting.', messageList)
                    hero.time += 15
                if enemy.c == 'R':
                    XP += 50
                    io.new_message('You get your thesis back!', messageList)
                    thesis = 1

        hero.leveluploop(XP)
        XP = 0

        # Rival information

        if thesis == 1 and rival not in lvl.enemylist:
            if random.random() < 0.05:
                r = random.randint(1, 3000)
                rival = ch.Enemy(lvl.getx(r), lvl.gety(r), 'R', 'Rival')
                lvl.enemylist.append(rival)
        if thesis == 1 and rival in lvl.enemylist:
            if ch.nextto(rival, hero):
                thesis = 0

        io.drawscreen(win, lvl, messageList, hero, thesis, dlvl, t, T)
        win.update()
        pygame.display.update()
        t += 1
        if t < hero.speedterminate:
            if (t % hero.speed) == 0:
                hero.time -= 1
        # ne stands for non-euclidean
        elif hero.ne == 1:
            hero.time -= nedist()
        elif thesis == 0:
            hero.time -= 1

        if newGame:
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
