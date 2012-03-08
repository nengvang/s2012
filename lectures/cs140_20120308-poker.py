"""Poker hands
0: Nothing in hand; not a recognized poker hand 
1: One pair; one pair of equal ranks within five cards 
2: Two pairs; two pairs of equal ranks within five cards 
3: Three of a kind; three equal ranks within five cards 
4: Straight; five cards, sequentially ranked with no gaps 
5: Flush; five cards with the same suit 
6: Full house; pair + different rank three of a kind 
7: Four of a kind; four equal ranks within five cards 
8: Straight flush; straight + flush 
9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush

Deck of cards representation (INTEGERS!!!!)
     0-51   All Cards
     0-12   Clubs       0
    13-25   Diamonds    1
    26-38   Hearts      2
    39-51   Spades      3

    0   Ace
    1   Deuce
    2   3
    3   4
    4   5
    ...
    9   10
    10  Jack
    11  Queen
    12  King

Hand of cards is a list of 5 cards (range 0-51)
"""

def print_card(card):
    faces = ['Ace of', '2 of', '3 of', '4 of', '5 of', '6 of', '7 of', '8 of',
             '9 of', '10 of', 'Jack of', 'Queen of', 'King of']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    print faces[card % 13], suits[card / 13]


def evaluate_hand(hand):        # [<c1>, <c2>, <c3>, <c4>, <c5>]
    # Start by sorting your hand
    hand.sort()

    # Sorted hands with royal flushes are one of
    if hand in [[0, 9, 10, 11, 12], [13, 22, 23, 24, 25],
                [26, 35, 36, 37, 38], [39, 48, 49, 50, 51]]:
        print 'Royal Flush'
        return 9
    
    # Finding a straight flush???
    suit = hand[0] / 13
    if hand[1] / 13 == suit and hand[2] / 13 == suit and hand[3] / 13 == suit and hand[4] / 13 == suit:
        flush = True;
    first = hand[0] % 13
    if hand[1] % 13 == first + 1 and hand[2] % 13 == first + 2 and hand[3] % 13 == first + 3 and hand[4] % 13 == first + 4:
        straight = True
    elif first == 0 and hand[1] % 13 == 9 and hand[2] % 13 == 10 and hand[3] % 13 == 11 and hand[4] % 13 == 12:
        straight = True
    else:
        straight = False
    if straight and flush:
        print 'Straight Flush'
        return 8

    if flush:
        print 'Flush'
        return 5

    if straight:
        print 'Straight'
        return 4
