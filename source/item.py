import io, characters, level, random

class Item(object):
	def __init__(self, name, posx, posy):
		self.name = name
		self.posx = posx
		self.posy = posy

	def getpos(self):
		return (self.posx, self.posy)

def useitem(name, messageList, hero, level, t):
	if name == 'coffee':
		return 0
		