'''
Created by sunwoong on 2023/02/16
'''
import sys
input = sys.stdin.readline

def binary_search(left, right, target):
    if left > right:
        return False
    mid = (left + right) // 2
    if items[mid] == target:
        return True
    elif items[mid] > target:
        return binary_search(left, mid - 1, target)
    return binary_search(mid + 1, right, target)

n = int(input())
items = sorted(list(map(int, input().split())))
m = int(input())
find_items = list(map(int, input().split()))
for item in find_items:
    print("yes") if binary_search(0, n - 1, item) else print("no")