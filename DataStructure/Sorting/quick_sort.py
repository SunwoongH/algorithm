from typing import List
import random

def partition(items: List[int], left: int, right: int) -> int:
    low, pivot_item = left - 1, items[right]
    for high in range(left, right):
        if items[high] < pivot_item:
            low += 1
            items[low], items[high] = items[high], items[low]
    items[low + 1], items[right] = items[right], items[low + 1]
    return low + 1

def quick_sort(items: List[int], left: int, right: int) -> None:
    if left < right:
        pivot = partition(items, left, right)
        quick_sort(items, left, pivot - 1)
        quick_sort(items, pivot + 1, right)

# Test
items = [random.randint(1, 100) for _ in range(10)]
print("before sorting: ", *items)
quick_sort(items, 0, len(items) - 1)
print("after sorting: ", *items)