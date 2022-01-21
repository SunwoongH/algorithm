'''
문제 - 두 용액

풀이 방법 - 정렬 후 투 포인터 활용하여 풀이.

>>> 항상 반례를 고민해보면서 문제를 풀이하자.
'''
import sys

n = int(sys.stdin.readline())
items = list(map(int, sys.stdin.readline().split()))
result = []
target = sys.maxsize
items.sort()
left, right = 0, n - 1
while left < right:
    sum_item = items[left] + items[right]
    if abs(sum_item) < target:
        target = abs(sum_item)
        if result:
            result.pop()
        result.append([items[left], items[right]])
    if sum_item < 0:
        left += 1
    else:
        right -= 1
print(*result[0])