import random


cardVal = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}


cards = []
answer = True

for i in range(3):
    key = random.choice(list(cardVal.keys()))
    cards.append(key)
print(cards)

total = 0
for card in cards:
    total += cardVal[card]

if 'A' in cards and total <= 10:
    total += 10

if total <= 17:
    print(total)
    answer = input('would you like to hit?\n > ').lower()
    if answer == 'yes':
        while total <= 17:
            card = random.choice(list(cardVal.keys()))
            cards.append(card)
            total += cardVal[card]
        print(cards, total)
    else:
        print(cards, total)

if 20 >= total >= 18:
    print(total, 'stay')

elif total == 21:
    print(total, 'blackjack')

elif total > 21:
    print(total, 'busted')
