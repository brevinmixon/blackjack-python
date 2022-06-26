from game import playgame
from make_deck import makedeck
import pygame
from display import window


def main():
    pygame.init()

    running = True
    pygame.display.set_mode((400, 500))
    color = (0, 255, 0)

    while running:



        # Initialing RGB Color
        color = (0, 255, 0)
        #surface.fill(color)
        pygame.display.flip()

        #get number of players function
        playgame()
        choice = 0
        while choice<1 or choice>2:
            print("Want to Play Again?")
            choice=input()     #make it so that input can only be a number
            choice=int(choice)
            if choice==1:
                choice=0
                playgame()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.quit()
    return





if __name__ == '__main__':
    main()

