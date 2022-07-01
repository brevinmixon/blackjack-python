import time
import pygame
from deck import newdeck
from PIL import Image
import random
import sys
import os

Green=(34,139,34)
White=(255,255,255)
FPS=60
Textcolor=(0,0,0)
#split hand
#sounds
#reveal dealers second, then sleep
#tally wins and loses
cw=60
ch=85


def main():
    pygame.init()  #does this need to be here or outside the function
    clock=pygame.time.Clock()
    pygame.display.set_caption('Blackjack Definitive Edition')
    font1 = pygame.font.SysFont('freesanbold.ttf', 50)
    font2 = pygame.font.SysFont('freesanbold.ttf', 40)
    text1 = font1.render('Press Spacebar to Play!', True, Textcolor)
    textRect1 = text1.get_rect()
    textRect1.center = (320, 210)
    text2 = font1.render('Press 1 to Hit, Press 2 to Stand', True, Textcolor)
    nulltext = font1.render('', True, Textcolor)
    #blankrect=
    textRect2= text2.get_rect()
    textRect2.center = (320, 210)
    wins=0
    losses=0

    running = True
    Win= pygame.display.set_mode((640, 420))  #expand to (800,500) to update menu
    init=False #initialized #outside or inside main???


    while running:
        #pygame.event.get()
        pygame.event.pump()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            Win.fill((50,50,50))
            pygame.draw.rect(Win, Green, pygame.Rect(0, 0, 640, 420))

            textdubs = font2.render(f'Wins: {wins}', True, White)
            textdubsR = textdubs.get_rect()
            textdubsR.center = (710, 220)
            #Win.blit(textdubs, textdubsR)


            textls = font2.render(f'Losses: {losses}', True, White)
            textlsR = textdubs.get_rect()
            textlsR.center = (710, 280)
            #Win.blit(textls, textlsR)

            if init==False:
                back = pygame.image.load('back.png').convert_alpha()
                pygame.Surface.convert_alpha(back)
                back = pygame.transform.scale(back, (60, 85))
                Win.blit(back, (560, 300)) #Player first card
                Win.blit(back, (485, 300))  # Player first card

                Win.blit(back, (20, 30))  #dealer face up
                Win.blit(back, (95,30))
                Win.blit(text1, textRect1)
                pygame.display.update()

                #Set Everything False
                getcards=False
                playerphase=False
                dealerphase=False
                showcards=False
                P2=False
                P3=False
                P4=False
                P5=False
                P6=False
                P7=False
                result=False
                bust=False
                tie=False
                win=False
                loss=False
                res=False
                checkedbj=False
                bjwin=False
                bjtie=False
                bjloss=False
                showdealer=False
                done=False
                player=[]
                dealer=[]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        init=True
                        getcards=True

            ############################
            #Now start the game



            if getcards==True:
                deck=newdeck()
                player = []
                dealer = []
                for i in range(2):
                    player.append(deck.pop())
                    dealer.append(deck.pop())
                print("Player's Cards: ", end="")
                print(player)
                print(f"Dealer's Cards: {dealer[0]}, ???")
                showcards=True
                getcards=False
                #playerphase=True
                checkedbj=True

            if showcards==True:
                P0=player[0][1]
                P1=player[1][1]
                D0=dealer[0][1]
                D1=dealer[1][1]

                P0 = pygame.image.load(P0).convert_alpha()
                pygame.Surface.convert_alpha(P0)
                P0= pygame.transform.scale(P0, (cw, ch))

                P1 = pygame.image.load(P1).convert_alpha()
                pygame.Surface.convert_alpha(P1)
                P1 = pygame.transform.scale(P1, (cw, ch))

                D0 = pygame.image.load(D0).convert_alpha()
                pygame.Surface.convert_alpha(D0)
                D0 = pygame.transform.scale(D0, (cw, ch))

                D1 = pygame.image.load(D1).convert_alpha()
                pygame.Surface.convert_alpha(D1)
                D1 = pygame.transform.scale(D1, (cw, ch))

                Win.blit(P0, (560, 300))  # Player first card
                Win.blit(P1, (485, 300))  # Player first card

                Win.blit(D0, (20, 30))  # dealer face up
                Win.blit(back, (95, 30))  #dealer face down
                #1pygame.display.update()

                #maybe display current score on table
                playerscore=score(player)
                dealerscore=score(dealer)
                print(playerscore)
                print(dealerscore)

            if checkedbj==True:
                #check for blackjack, #print result onto screen
                if  playerscore== 21 and dealerscore == 21:
                    print("Blacjack. Tie.")
                    Win.blit(back, (95, 30))
                    pygame.display.update()
                    res=True
                    #Play again?
                elif playerscore == 21:
                    print("Player 1 Wins")
                    Win.blit(back, (95, 30))
                    pygame.display.update()
                    res=True
                    #Play again?
                elif dealerscore == 21:
                    print("Dealer Wins")
                    Win.blit(back, (95, 30))
                    pygame.display.update()
                    res=True
                    #Play again?
                else:
                    checkedbj=False
                    playerphase=True


            if init==True: #Shows Cards 3-8
                if len(player)>2:
                    P2 = player[2][1]
                    P2 = pygame.image.load(P2).convert_alpha()
                    pygame.Surface.convert_alpha(P2)
                    P2 = pygame.transform.scale(P2, (cw, ch))
                    Win.blit(P2,(410,300))
                if len(player)>3:
                    P3 = player[3][1]
                    P3 = pygame.image.load(P3).convert_alpha()
                    pygame.Surface.convert_alpha(P3)
                    P3 = pygame.transform.scale(P3, (cw, ch))
                    Win.blit(P3, (335, 300))
                if len(player)>4:
                    P4 = player[4][1]
                    P4 = pygame.image.load(P4).convert_alpha()
                    pygame.Surface.convert_alpha(P4)
                    P4 = pygame.transform.scale(P4, (cw, ch))
                    Win.blit(P4, (260, 300))
                if len(player)>5:
                    P5 = player[5][1]
                    P5 = pygame.image.load(P5).convert_alpha()
                    pygame.Surface.convert_alpha(P5)
                    P5 = pygame.transform.scale(P5, (cw, ch))
                    Win.blit(P5, (185, 300))
                if len(player)>6:
                    P6 = player[6][1]
                    P6 = pygame.image.load(P6).convert_alpha()
                    pygame.Surface.convert_alpha(P6)
                    P6 = pygame.transform.scale(P6, (cw, ch))
                    Win.blit(P6, (110, 300))
                if len(player)>7:
                    P7 = player[7][1]
                    P7 = pygame.image.load(P7).convert_alpha()
                    pygame.Surface.convert_alpha(P7)
                    P7 = pygame.transform.scale(P7, (cw, ch))
                    Win.blit(P7, (35, 300))
                if len(dealer)>2:
                    D2 = dealer[2][1]
                    D2 = pygame.image.load(D2).convert_alpha()
                    pygame.Surface.convert_alpha(D2)
                    D2 = pygame.transform.scale(D2, (cw, ch))
                    Win.blit(D2, (170, 30))
                if len(dealer)>3:
                    D3 = dealer[3][1]
                    D3 = pygame.image.load(D3).convert_alpha()
                    pygame.Surface.convert_alpha(D3)
                    D3 = pygame.transform.scale(D3, (cw, ch))
                    Win.blit(D3, (245, 30))
                if len(dealer)>4:
                    D4 = dealer[4][1]
                    D4 = pygame.image.load(D4).convert_alpha()
                    pygame.Surface.convert_alpha(D4)
                    D4 = pygame.transform.scale(D4, (cw, ch))
                    Win.blit(D4, (320, 30))
                if len(dealer)>5:
                    D5 = dealer[5][1]
                    D5 = pygame.image.load(D5).convert_alpha()
                    pygame.Surface.convert_alpha(D5)
                    D5 = pygame.transform.scale(D5, (cw, ch))
                    Win.blit(D5, (395, 30))
                if len(dealer)>6:
                    D6 = dealer[6][1]
                    D6 = pygame.image.load(D6).convert_alpha()
                    pygame.Surface.convert_alpha(D6)
                    D6 = pygame.transform.scale(D6, (cw, ch))
                    Win.blit(D6, (470, 30))
                if len(dealer)>7:
                    D7 = dealer[7][1]
                    D7 = pygame.image.load(D7).convert_alpha()
                    pygame.Surface.convert_alpha(D7)
                    D7 = pygame.transform.scale(D7, (cw, ch))
                    Win.blit(D7, (545, 30))
                if showdealer==True:
                    Win.blit(D1, (95, 30))

            # Player Phase, How do i get it to wait for me
                    #Shows Cards 3-8
            if playerphase==True and checkedbj==False:
                Win.blit(text2, textRect2)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        player.append(deck.pop())
                        if score(player)>21:
                            res=True
                            bust=True
                            playerphase=False
                    if event.key == pygame.K_2:
                        playerphase=False
                        dealerphase=True
                        showdealer=True

                        #Win.blit(text2,textRect2)
                        Win.blit(D1, (95, 30))
                        pygame.display.update()

            if dealerphase==True:
                if score(dealer)>16:
                    dealerphase==False
                    res=True
                else:
                    time.sleep(1)
                    dealer.append(deck.pop(0))



            #reset
            if res==True:
                if score(player)>21:
                    losses+=1
                    textbust = font1.render('Bust!  Space to Play, Q to Quit', True, Textcolor)
                    textbustR = textbust.get_rect()
                    textbustR.center = (320, 210)
                    Win.blit(textbust,textbustR)
                elif score(dealer)>21:
                    wins+=1
                    textbust2 = font1.render('Dealer Busts! Space to Play, Q to Quit', True, Textcolor)
                    textbust2R= textbust2.get_rect()
                    textbust2R.center = (320, 210)
                    Win.blit(textbust2, textbust2R)
                elif score(player)>score(dealer):
                    wins+=1
                    textwin = font1.render('You Win! Space to Play, Q to Quit', True, Textcolor)
                    textwinR = textwin.get_rect()
                    textwinR.center = (320, 210)
                    Win.blit(textwin, textwinR)
                elif score(dealer)>score(player):
                    losses+=1
                    textlose = font1.render('You Lost! Space to Play, Q to Quit', True, Textcolor)
                    textloseR = textlose.get_rect()
                    textloseR.center = (320, 210)
                    Win.blit(textlose, textloseR)
                elif score(dealer)==score(player):
                    texttie = font1.render('Tie! Space to Play, Q to Quit', True, Textcolor)
                    textieR = texttie.get_rect()
                    texttieR.center = (320, 210)
                    Win.blit(texttie, texttieR)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        init=False
                    if event.key == pygame.K_q:
                        pygame.quit()
            pygame.display.update()

    pygame.quit()


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
    if aces==0 or sum<22:
        return sum

    while aces>0:
        if sum<22:
            break
        aces-=1
        sum-=10
    return sum

if __name__ == '__main__':
    main()

