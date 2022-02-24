from typing import List
import random

def bubble_sort(items: List[int]) -> None:
    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

# Test
items = [random.randint(1, 100) for _ in range(10)]
print("before sorting: ", *items)
bubble_sort(items)
print("after sorting: ", *items)