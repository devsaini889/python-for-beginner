# A simple program to shuffle the deck of cards

import random,itertools

deck = list(itertools.product(range(1,14) ,["Spade","club","Heart","Diamond"]))

random.shuffle(deck)
print(deck)

for i in range(5):
    print(deck[i][0] ,"of", deck[i][1])