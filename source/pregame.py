import pygame


def pregameLoop(win):
	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	tmp = 'hi'
	with open('title.txt', 'r') as f:
		for i, line in enumerate(f):
			win.write(line, 0, i, fgcolor=(0,0+10*i,255 - 10*i))
	win.update()
	pygame.display.update()

	e = pygame.event.wait()
	pressed = e.key

	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	win.write('What is your field of study?', 2, 5, fgcolor='white')
	win.write('a. Mathematics', 2, 7, fgcolor='white')
	win.write('b. Literature', 2, 8, fgcolor='white')
	win.write('c. Music', 2, 9, fgcolor='white')
	win.write('Default: General Studies (not recommended)', 2, 11, fgcolor='red')
	win.update()
	pygame.display.update()

	e = pygame.event.wait()
	pressed = e.key

	if pressed == 97:
		tmp = 'math'
	elif pressed == 98:
		tmp = 'lit'
	elif pressed == 99:
		tmp = 'music'

	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	win.write('Your rival has stolen your thesis the night before your defense. ', 5, 9, fgcolor=(0, 240, 10))
	win.write('He is uploading it the internet to pass it off as his own.', 5, 11, fgcolor=(0,240,10))
	win.write('You must get it from him in his office on the top floor,', 5, 13, fgcolor=(0,240,10))
	win.write('then safely exit the building.', 5, 14, fgcolor=(0,240,10))
	win.update()
	pygame.display.update()

	return tmp
