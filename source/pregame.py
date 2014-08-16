import pygcurse, pygame

def pregameLoop(win):
	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	tmp = 'hi'
	i = 0
	f = open('title.txt', 'r')
	for line in f:
		win.write(line, 0, i, fgcolor=(0,0+10*i,255 - 10*i))
		i += 1
	win.update()
	pygame.display.update()

	e = pygame.event.wait()
	pressed = e.key

	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	win.write('What is your field of study?', 2, 5, fgcolor='white')
	win.write('a. Mathematics', 2, 7)
	win.write('b. Literature', 2, 8)
	win.write('c. Music', 2, 9)
	win.update()
	pygame.display.update()

	e = pygame.event.wait()
	pressed = e.key

	if pressed == 97:
		tmp = 'math'
	if pressed == 98:
		tmp = 'lit'
	if pressed == 99:
		tmp = 'music'

	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	win.write('Your rival has stolen your thesis the night before your defense. ', 5, 9, fgcolor=(0, 240, 10))
	win.write('He is uploading it the internet to pass it off as his own.', 5, 11, fgcolor=(0,240,10))
	win.write('You must get it from him in his office on the top floor,', 5, 13, fgcolor=(0,240,10))
	win.write('then safely exit the building.', 5, 14, fgcolor=(0,240,10))
	win.update()
	pygame.display.update()

	return tmp