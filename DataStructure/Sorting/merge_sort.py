from typing import List
import random

def merge(items: List[int], left: int, mid: int, right: int) -> None:
    temp = [0 for _ in range(len(items))]
    i = left; j = mid + 1; k = left
    while i <= mid and j <= right:
        if items[i] <= items[j]:
            temp[k] = items[i]; i += 1
        else:
            temp[k] = items[j]; j += 1
        k += 1
    while i <= mid:
        temp[k] = items[i]; k += 1; i += 1
    while j <= right:
        temp[k] = items[j]; k += 1; j += 1
    for l in range(left, right + 1):
        items[l] = temp[l]

def merge_sort(items: List[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        merge_sort(items, left, mid)
        merge_sort(items, mid + 1, right)
        merge(items, left, mid, right)
        
# Test
items = [random.randint(1, 100) for _ in range(10)]
print("before sorting: ", *items)
merge_sort(items, 0, len(items) - 1)
print("after sorting: ", *items)