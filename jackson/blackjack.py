import random

#
# print "Player 1, what is your name?"
# player1 = raw_input()
#
# print player1
#
# print "Player 2, what is your name?"
# player2 = raw_input()
#
# print player2

player1 = "jackson"
player2 = "rob"


deck = [ 2, 2, 2, 2,
         3, 3, 3, 3,
         4, 4, 4, 4,
         5, 5, 5, 5,
         6, 6, 6, 6,
         7, 7, 7, 7,
         8, 8, 8, 8,
         9, 9, 9, 9,
         10, 10, 10, 10 ]

print "\n\nThe deck of cards:\n"
print deck

# Shuffle the deck
random.shuffle(deck)

print "\n\nShuffling:\n"
# print deck
print "\n"

# Give the player two random cards
print player1 + ", your cards are"

card1 = deck.pop()

card2 = deck.pop()
player1_total = card1 + card2
print str(card1) + " " + str(card2) + "     Your total is " + str(player1_total)


print "\n"
print deck

print player2 + ", your cards are here"
card3=deck.pop()
card4=deck.pop()
player2_total = card3 + card4
print str(card3) + " " + str(card4) + "     Your total is " + str(player2_total)

print "\n\n"

print player1 + ", your total is " + str(card1 + card2)
print "Would you like to hit (y/n)"
answer = raw_input()

if(answer=="y"):
    hitcard = deck.pop()
    print hitcard
    player1_total = hitcard + player1_total
    print player1 + " your new total is " + str(player1_total)



print player2 + ", your total is " + str(card1 + card2)
print "would you like to hit (y/n)"
answer = raw_input()

if (answer =="y"):
    hitcard = deck.pop()
    print hitcard
    player2_total = hitcard + player2_total
    print player2 + " your new total is " + str(card3+card4)
