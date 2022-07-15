'''
Created by sunwoong on 2022/07/15
'''
n = int(input())
prices = sorted(list(map(int, input().split())))
m = int(input())
if sum(prices) <= m:
    print(prices[-1])
else:
    left, right = 0, prices[-1]
    while left <= right:
        mid = (left + right) // 2
        temp = sum(map(lambda x: x if x < mid else mid, prices))
        if temp <= m:
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1)