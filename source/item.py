import io, characters, level, random

class Item(object):
	def __init__(self, name, posx, posy):
		self.name = name
		self.posx = posx
		self.posy = posy

	def getpos(self):
		return (self.posx, self.posy)

def useitem(name, messageList, hero, lvl, t):
	if name == 'coffee':
		hero.speed = 3
		hero.speedterminate = t + 100
		io.newMessage('You feel fast!', messageList)
	if name == 'tea':
		hero.skillcount = 5
		io.newMessage('You feel revitalized!', messageList)
	if name == 'ramen noodles':
		io.newMessage('Gain XP.', messageList)
		return 50
	if name == 'laptop':
		hero.v = 7
		io.newMessage('Viruses stall your rival for longer.', messageList)
	if name == 'beer':
		hero.strength += 1
		io.newMessage('You think you are stronger.', messageList)
	if name == 'glasses':
		io.newMessage('You can read book titles from far away.', messageList)
	if name == 'moleskin':
		io.newMessage('You start taking notes.', messageList)
	return 0


		