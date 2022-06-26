import pygame
def window():

    pygame.init()

    running = True
    pygame.display.set_mode((400, 500))

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    # Initialing RGB Color
    color = (255, 0, 0)

    # Changing surface color
    surface.fill(color)
    pygame.display.flip()