'''
Created by sunwoong on 2025/09/14
'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ban = [False for _ in range(n + 1)]
if m != 0:
    temp = list(map(int, sys.stdin.readline().split()))
    for num in temp:
        ban[num] = True

dp = [[sys.maxsize for _ in range(41)] for _ in range(n + 1)]

def bfs(start):
    queue = deque([(start, 0)])
    dp[start][0] = 0

    while queue:
        day, coupon = queue.popleft()

        for standard in range(1, 6, 2):
            next_day = day + standard
            if next_day > n:
                continue
            if standard == 1:
                if ban[next_day]:
                    dp[next_day][coupon] = min(dp[next_day][coupon], dp[day][coupon])
                    queue.append((next_day, coupon))
                    break
                if coupon >= 3 and dp[next_day][coupon - 3] > dp[day][coupon]:
                    dp[next_day][coupon - 3] = dp[day][coupon]
                    queue.append((next_day, coupon - 3))
                if dp[next_day][coupon] > dp[day][coupon] + 10000:
                    dp[next_day][coupon] = dp[day][coupon] + 10000
                    queue.append((next_day, coupon))
            if standard == 3:
                if dp[next_day][coupon + 1] > dp[day][coupon] + 25000:
                    dp[next_day][coupon + 1] = dp[day][coupon] + 25000
                    queue.append((next_day, coupon + 1))
            if standard == 5:
                if dp[next_day][coupon + 2] > dp[day][coupon] + 37000:
                    dp[next_day][coupon + 2] = dp[day][coupon] + 37000
                    queue.append((next_day, coupon + 2))

bfs(0)
print(min(dp[n]))