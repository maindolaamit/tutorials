"""
Create a deck of cards sequence using zip. Each card is represented as tuple
holding number 1-13 and a Character 'S', 'H', 'D', 'A' corresponding to Space, Heart, Diamond and Club.

Show 3 random Cards pulled from Deck
"""

import random

numbers = [i for i in range(1, 14)] * 4
card = 'S' * 13 + 'H' * 13 + 'D' * 13 + 'C' * 13
deck = list(zip(numbers, card))
# Print the deck - 10 cards
print("All cards in the Deck")
print(deck[0:5])

# View a Sample
print("\nRandom Samples taken from Deck")
print(random.sample(deck, 10))

# Take out Random card
print("\nRandon Choices made from Deck")
for i in range(3):
    print(format(random.choice(deck)))
print("")

# Shuflle the cards
random.shuffle(deck)
# Print the deck - 10 cards
print("\nAfter Shuffling the Cards")
print(deck[0:5])
