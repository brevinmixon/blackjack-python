# This is a sample Python script.
import random


def make_deck():
    suits=["Hearts", "Clubs", "Spades", "Diamonds"]
    ranks=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    deck=[]
    for i in range(13):
        for j in range(4):
            deck.append([ranks[i],suits[j]])
    random.shuffle(deck)
    return deck

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hello, B ")  # Press Ctrl+F8 to toggle the breakpoint.

    deck=make_deck()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
