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
		tmp == 'lit'
	if pressed == 99:
		tmp == 'music'

	win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
	win.write('Your rival has stolen your thesis', 5, 9, fgcolor='white')
	win.write('the night before your defense. ', 5, 10, fgcolor='white')
	win.write('He is attempting to upload it ', 5, 11, fgcolor='white')
	win.write('to the internet to pass it', 5, 12, fgcolor='white')
	win.write('off as his own. ', 5, 13, fgcolor='white')
	win.write('You must get it from him', 5, 14, fgcolor='white')
	win.write('in his office on the top floor and safely', 5, 15, fgcolor='white')
	win.write('return to your own office (in another building).', 5, 16, fgcolor='white')
	win.update()
	pygame.display.update()

	return tmp