import pygcurse, pygame


def pregameLoop(win):
	a = []
	f = open('title.txt', 'r')
	for line in f:
		a.append(line)
	for i in range(len(a)):
		win.write(a[i], 0, i, fgcolor='white')
	win.update()
	pygame.display.update()
	
	pygame.event.set_allowed(None)
	pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
	e = pygame.event.wait()
	pressed = e.key

	win.fill(' ', region = (0, 0, 60, 30), fgcolor='black', bgcolor='black')
	win.write('What is your field of study?', 0, 5, fgcolor='white')
	win.write('a. Mathematician', 0, 7)
	win.write('b. Literature', 0, 8)
	win.write('c. Music', 0, 9)
	win.update()
	pygame.display.update()

	pygame.event.set_allowed(None)
	pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
	e = pygame.event.wait()
	pressed = e.key
