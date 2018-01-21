# Write a method to shu e a deck of cards It must be a perfect shu e - in other
# words, each52!permutationsofthedeckhastobeequallylikely Assumethatyouaregiven
# a random number generator which is perfect

import random
import math

def shuffle(deck):
    used_pos = set()
    for i in xrange(len(deck)):
        if i in used_pos:
            continue
        target = int(math.floor(random.random() * len(deck)))
        while target in used_pos or target == i:
            target = int(math.floor(random.random() * len(deck)))

        used_pos.add(i)
        used_pos.add(target)
        deck[target] ^= deck[i]
        deck[i] ^= deck[target]
        deck[target] ^= deck[i]
        
    return deck

deck = []
for i in xrange(52):
    deck.append(i+1)

print shuffle(deck)
