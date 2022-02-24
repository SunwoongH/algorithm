from typing import List
import random

def insertion_sort_v1(items: List[List]) -> None:
    for i in range(1, len(items)):
        loc = i - 1
        item = items[i]
        while loc >= 0 and item < items[loc]:
            items[loc + 1] = items[loc]
            loc -= 1
        items[loc + 1] = item
        
def insertion_sort_v2(items: List[List]) -> None:
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1

# Test
items = [random.randint(1, 100) for _ in range(10)]
print("before sorting: ", *items)
insertion_sort_v1(items)
print("after sorting: ", *items)