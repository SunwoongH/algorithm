'''
Created by sunwoong on 2025/08/15
'''
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
location = [1 for _ in range(n)]

max_value = 0
basket = []
answer = int(1e9)

for i in range(n):
    ability[i].sort()
    heapq.heappush(basket, ((ability[i][0]), ability[i][0], i))
    max_value = max(max_value, ability[i][0])

while basket:
    _, value, row = heapq.heappop(basket)

    answer = min(answer, max_value - value)

    if location[row] == m:
        break

    heapq.heappush(basket, ((ability[row][location[row]]), ability[row][location[row]], row))
    max_value = max(max_value, ability[row][location[row]])
    location[row] += 1

print(answer)