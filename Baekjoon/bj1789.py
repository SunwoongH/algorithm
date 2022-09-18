'''
Created by sunwoong on 2022/09/18
'''
import sys

def binary_search(left: int, right: int):
    if left > right:
        return left
    mid = (left + right) // 2
    if (mid * (mid + 1) // 2) > n:
        return binary_search(left, mid - 1)
    else:
        return binary_search(mid + 1, right)

n = int(sys.stdin.readline())
print(binary_search(1, n) - 1) if n != 1 else print(1)