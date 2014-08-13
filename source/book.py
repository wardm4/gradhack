import io, characters, level, random

class Book(object):
	def __init__(self, name, posx, posy):
		self.name = name
		self.posx = posx
		self.posy = posy

	def getpos(self):
		return (self.posx, self.posy)

def usebook(name, messageList, hero, level, t):
	if name == 'hp':
		io.newMessage('You find the book Harry Potter.', messageList)
		io.newMessage('It distracts you for 1 turn.', messageList)
		hero.time -= 1
	if name == 'lotr':
		io.newMessage('You find The Lord of the Rings.', messageList)
		io.newMessage('It distracts you for 3 turns.', messageList)
		hero.time -= 3
	if name == 'ij':
		io.newMessage('You find Infinite Jest.', messageList)
		io.newMessage('It distracts you for 5 turns.', messageList)
		hero.time -= 5
	if name == 'got':
		io.newMessage('You find Game of Thrones.', messageList)
		io.newMessage('It distracts you for 7 turns.', messageList)
		hero.time -= 7
	if name == 'wot':
		io.newMessage('You find The Wheel of Time.', messageList)
		io.newMessage('It distracts you for 10 turns.', messageList)
		hero.time -= 10
	if name == 'qm':
		io.newMessage('You find a Quantum Mechanics Textbook.', messageList)
		if random.random() < 0.1:
			r = random.randint(1,3000)
			hero.posx = level.getx(r)
			hero.posy = level.gety(r)
		else:
			hero.posx = level.end[0]
			hero.posy = level.end[1]
	if name == 'bio':
		io.newMessage('You find a Biochemistry Textbook.', messageList)
		io.newMessage('Your skills recharge.', messageList)
		level.skillcount = 3
	if name == 'bhot':
		io.newMessage('You find A Brief History of Time.', messageList)
		io.newMessage('You gain 10 time.', messageList)
		hero.time += 10
	if name == 'pharma':
		io.newMessage('You find a Pharmacology Textbook.', messageList)
		io.newMessage('You make speed.', messageList)
		hero.speed = 2
		hero.speedterminate = t + 20
	if name == 'eos':
		io.newMessage('You find The Elements of Style.', messageList)
		io.newMessage('Gain 20 XP.')
		hero.xp += 20

