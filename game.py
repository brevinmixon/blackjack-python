from make_deck import makedeck
from getsum import score


def playgame():
    deck=makedeck()

    player=[]
    dealer=[]
    for i in range(2):
        player.append(deck.pop())
        dealer.append(deck.pop())
    print("Player's Cards: ", end="")
    print(player)
    print(f"Dealer's Cards: {dealer[0]}, ???" )



    #Check for Blackjack for all players
    if score(player)==21 and score(dealer)==21:
        print("Blacjack. Tie.")
        return
    elif score(player)==21:
        print("Player 1 Wins")
        return
    elif score(dealer)==21:
        print("Dealer Wins")
        return

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


















if __name__=="__playgame__":
    playgame()