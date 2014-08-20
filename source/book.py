import io
import characters
import level
import random


class Book(object):
    def __init__(self, name, posx, posy):
        self.name = name
        self.posx = posx
        self.posy = posy

    def getpos(self):
        return (self.posx, self.posy)


def usebook(name, messageList, hero, lvl, t):
    if name == 'Harry Potter':
        io.new_message('You find the book Harry Potter.', messageList)
        io.new_message('It distracts you for 1 turn.', messageList)
        hero.time -= 1
    if name == 'Lord of the Rings':
        io.new_message('You find The Lord of the Rings.', messageList)
        io.new_message('It distracts you for 3 turns.', messageList)
        hero.time -= 3
    if name == 'Infinite Jest':
        io.new_message('You find Infinite Jest.', messageList)
        io.new_message('It distracts you for 5 turns.', messageList)
        hero.time -= 5
    if name == 'Game of Thrones':
        io.new_message('You find Game of Thrones.', messageList)
        io.new_message('It distracts you for 7 turns.', messageList)
        hero.time -= 7
    if name == 'Wheel of Time':
        io.new_message('You find The Wheel of Time.', messageList)
        io.new_message('It distracts you for 10 turns.', messageList)
        hero.time -= 10
    if name == 'Quantum Mechanics':
        io.new_message('You find a Quantum Mechanics Textbook.', messageList)
        if random.random() < 0.1:
            r = random.randint(1, 3000)
            hero.posx = lvl.getx(r)
            hero.posy = lvl.gety(r)
        else:
            hero.posx = lvl.end[0]
            hero.posy = lvl.end[1]
    if name == 'Biochemistry':
        io.new_message('You find a Biochemistry Textbook.', messageList)
        io.new_message('Your skills recharge.', messageList)
        lvl.skillcount = 3
    if name == 'Brief History of Time':
        io.new_message('You find A Brief History of Time.', messageList)
        io.new_message('You gain 10 time.', messageList)
        hero.time += 10
    if name == 'Pharmacology':
        io.new_message('You find a Pharmacology Textbook.', messageList)
        io.new_message('You make speed.', messageList)
        hero.speed = 2
        hero.speedterminate = t + 20
    if name == 'The Elements of Style':
        io.new_message('You find The Elements of Style.', messageList)
        io.new_message('Gain 20 XP.', messageList)
        return 20
    return 0
