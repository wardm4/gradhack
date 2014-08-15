import pygcurse, pygame
print pygame.font.get_fonts()

print range(6)
print pygcurse.colornames

win = pygcurse.PygcurseWindow(20, 10)
font = pygame.font.SysFont('arial', 24, bold=False, italic=False)
win.write('The Ojibway aboriginal people in North America used cowry shells which they called sacred Miigis Shells.')
pygcurse.waitforkeypress()
win.font = pygame.font.SysFont('liberationserif', 24, bold=False, italic=False)
pygcurse.waitforkeypress()
