import random

def makedeck():
    suits=["Hearts", "Clubs", "Spades", "Diamonds"]
    ranks=[2, 3, 4, 5, 6, 7, 8, 9 , 10, "J", "Q", "K", "A"]
    deck=[]
    for i in range(13):
        for j in range(4):
            deck.append([ranks[i],suits[j]])
    random.shuffle(deck)
    return deck