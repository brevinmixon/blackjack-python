#from game import playgame
from make_deck import makedeck
import pygame
from deck import newdeck
from PIL import Image
import random
import sys
import os
from test import test69
Green=(0,255,0)
FPS=60
#to do list:
#press 1 to play, initilize with back of cards
#press to play again
#split hand
#display current score
#sounds
#reveal dealers second card



#Cardwith=
#Cardheight=


def main():
    pygame.init()  #does this need to be here or outside the function
    clock=pygame.time.Clock()

    running = True
    Win= pygame.display.set_mode((800, 500))
    start=False
    getcards=False
    playerphase=False
    dealerphase=False


    while running:
        #pygame.event.get()
        pygame.event.pump()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Win.fill(Green)

            table=pygame.image.load('table.png').convert_alpha()
            pygame.Surface.convert_alpha(table)
            table = pygame.transform.scale(table, (800, 500))
            Win.blit(table,(0,0))

            back = pygame.image.load('back.png').convert_alpha()
            pygame.Surface.convert_alpha(back)
            back = pygame.transform.scale(back, (40, 65))
            Win.blit(back, (380, 350)) #Player first card
            Win.blit(back, (390, 340))  # Player first card

            Win.blit(back, (400, 65))  #dealer face up
            Win.blit(back, (380, 65))

            if start==False:
                pygame.display.update()
                start=True

            # testimage
            img = pygame.image.load('img.png').convert_alpha()
            pygame.Surface.convert_alpha(img)
            img = pygame.transform.scale(img, (40, 65))


            ############################ How do i get it to do something once
            #Now start the game
            #Attach the .png to the card info

            #Make an input to press 1 to start the game, word box that says press 1 to Play
            #if event.type == pygame.K_1:

            if getcards==False:
                deck=newdeck()
                player = []
                dealer = []
                for i in range(2):
                    player.append(deck.pop())
                    dealer.append(deck.pop())


                print("Player's Cards: ", end="")
                print(player)
                print(f"Dealer's Cards: {dealer[0]}, ???")

                P0=player[0][1]
                P1=player[1][1]
                D0=dealer[0][1]
                D1=dealer[1][1]

                P0 = pygame.image.load(P0).convert_alpha()
                pygame.Surface.convert_alpha(P0)
                P0= pygame.transform.scale(P0, (40, 65))

                P1 = pygame.image.load(P1).convert_alpha()
                pygame.Surface.convert_alpha(P1)
                P1 = pygame.transform.scale(P1, (40, 65))

                D0 = pygame.image.load(D0).convert_alpha()
                pygame.Surface.convert_alpha(D0)
                D0 = pygame.transform.scale(D0, (40, 65))

                D1 = pygame.image.load(D1).convert_alpha()
                pygame.Surface.convert_alpha(D1)
                D1 = pygame.transform.scale(D1, (40, 65))

                Win.blit(P0, (380, 350))  # Player first card
                Win.blit(P1, (390, 340))  # Player first card

                Win.blit(D0, (400, 65))  # dealer face up
                Win.blit(back, (380, 65))  #dealer face down
                pygame.display.update()

                #maybe display current score on table
                playerscore=score(player)
                dealerscore=score(dealer)
                print(playerscore)
                print(dealerscore)

                #check for blackjack, #print result onto screen
                if  playerscore== 21 and dealerscore == 21:
                    print("Blacjack. Tie.")
                    #Play again?
                elif playerscore == 21:
                    print("Player 1 Wins")
                    #Play again?
                elif dealerscore == 21:
                    print("Dealer Wins")
                    #Play again?
            getcards=True

            # Player Phase, How do i get it to wait for me
            if playerphase==False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        player.append(deck.pop())
                        print(player)
                        #continue here, check score
                    if event.key == pygame.K_2:
                        playerphase=True


            #if event.type == pygame.KEYDOWN:








    pygame.quit()

    #Maybe i should i put play again here
    return



def playgame(Win):






    #Player Phase
    while True:
        choice=0
        while choice<1 or choice>2:
            choice=input("1: Hit,     2: Stand")
            print(choice)
            choice=int(choice)
        if choice==2:
            break
        if choice==1:
            player.append(deck.pop())
            print(player)
        if score(player)>21:
            print("Player Busts")
            return

    #Dealer Phase
    while score(dealer)<17:
        dealer.append(deck.pop())
    if score(dealer)>21:
        print("Dealer Busts")
        return

    #Check Scores
    if score(player)==score(dealer):
        print("Tie")
        return
    elif score(player)>score(dealer):
        print("Player Wins!")
        return
    else:
        print("Dealer Wins")
        return

def score(list):

    sum=0
    aces=0
    for i in range(len(list)):
        if list[i][0]=="J" or list[i][0]=="Q" or list[i][0]=="K":
            sum+=10
        elif list[i][0]=="A":
            sum+=11
            aces+=1
        else:
            sum+=list[i][0]
    if sum>21 and aces==0:
        return sum

    while aces>0:
        if sum<22:
            break
        aces-=1
        sum-=10
    return sum

if __name__ == '__main__':
    main()

