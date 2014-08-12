import pygcurse, pygame

def pregameLoop(win):
	tmp = 'hi'
	i = 0
	f = open('title.txt', 'r')
	for line in f:
		win.write(line, 0, i, fgcolor='white')
		i += 1
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

	if pressed == 97:
		tmp = 'math'
	if pressed == 98:
		tmp == 'lit'
	if pressed == 99:
		tmp == 'music'

	win.fill(' ', region = (0, 0, 60, 30), fgcolor='black', bgcolor='black')
	win.write('Your rival has stolen your thesis \n the night before your defense. \n He is attempting to upload it \n to the internet to pass it' \
			'off as his own. \n You must get it from him \n in his office on the top floor and safely \n return to your own office \n' \
			'(in another building).', 0, 9, fgcolor='white')
	win.update()
	pygame.display.update()

	return tmp