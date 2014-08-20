import pygcurse, pygame, time

def loseloop(win):
    win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
    with open('lose.txt', 'r') as f:
        for i, line in enumerate(f):
            win.write(line, 0, i, fgcolor=(255-2*i,4*i,2*i))
    win.update()
    pygame.display.update()

    time.sleep(3)
    e = pygame.event.wait()
    pressed = e.key

def winloop(win):
    win.fill(' ', region = (0, 0, 70, 35), fgcolor='black', bgcolor='black')
    with open('win.txt', 'r') as f:
        for i, line in enumerate(f):
            win.write(line, 0, i, fgcolor=(10*i,0,255 - 10*i))
    win.update()
    pygame.display.update()

    time.sleep(3)
    e = pygame.event.wait()
    pressed = e.key
