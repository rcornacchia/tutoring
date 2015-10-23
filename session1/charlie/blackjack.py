import random


name = "Charlie"

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

print deck

# Give the player two random cards

# Ask them if they want to stay or hit

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
