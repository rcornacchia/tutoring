import random

# print name + " is a programmer"
print "\n\nThis is the deck of cards:\n"
# Create an empty list of cards
deck = [2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4,
        5, 5, 5, 5,
        6, 6, 6, 6,
        7, 7, 7, 7,
        8, 8, 8, 8,
        9, 9, 9, 9,
        10, 10, 10, 10]


print deck
print "\n\nShuffling cards\n"

random.shuffle(deck)

# Give the player two random cards
print "Player 1"
card1 = deck.pop()
print "Your first card is " + str(card1)
# print deck
card2 = deck.pop()
print "your second card is " + str(card2)
player1_total = card1 + card2

# Repeat for player 2
print "Player 2"
card3 = deck.pop()
print "Your first card is" + str(card3)
# print deck
card4 = deck.pop()
print "Your second card is " + str(card4)
player2_total = card3 + card4

hitAgain = False

# Ask them if they want to stay or hit
print "Player 1, your total is: " + str(card1 + card2) + "\nWould you like to hit (yes/no)?"
answer = raw_input()

print "You answered " + answer

if(answer == "yes"):
    extra_card = deck.pop()
    print extra_card
    player1_total = player1_total + extra_card
    print "Your new total is" + str(player1_total)
    if(player1_total>21):
        print "\n your busted Player2 wins!! \n"
        exit()

elif(answer == "cheat"):
    player1_total = 21

# Repeat for Player 2
print "\nplayer 2 your total is: " + str(card3 + card4 ) + "\nWould you like to hit (yes/no)?"
answer2 = raw_input()

print "You answered " + answer2

if(answer2 == "yes"):
    extra_card2 = deck.pop()
    print extra_card2
    player2_total = player2_total + extra_card2
    print "Your new total is " + str(player2_total)
    if(player2_total>21):
        print "\n your busted Player1 wins!!!"
        exit()
if(player1_total > player2_total):
    print "Player 1 wins!!!"
elif(player1_total == player2_total):
    print "There is a tie!!!!"
else:
    print "Player 2 wins!!!"
if (player1_total == 21):
    print "blackjack!!"

if(player2_total == 21):
    print "blackjack!!"
# A deck of cards consists of 4 of each:
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# J = 10
# Q = 10
# K = 10
# A = 11
