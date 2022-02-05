import sys

n, m = map(int, sys.stdin.readline().split())
cards = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

def find_card(n, m, cards):
    sum = 0
    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) - 1):
            for k in range(j + 1, len(cards)):
                temp = cards[i] + cards[j] + cards[k]
                if temp == m:
                    sum = temp
                    return sum
                elif temp > sum and temp < m:
                    sum = temp
    return sum
print(find_card(n, m, cards))