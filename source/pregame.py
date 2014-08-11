import pygcurse, pygame

def pregameLoop():
	while True:
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

        False