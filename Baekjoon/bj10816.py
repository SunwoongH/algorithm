import sys
from collections import defaultdict

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find_cards = list(map(int, sys.stdin.readline().split()))

card_table = defaultdict(int)
for card in cards:
    card_table[card] += 1
for card in find_cards:
    if card in card_table:
        print(card_table.get(card), end=' ')
    else:
        print(0, end=' ')