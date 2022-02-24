from typing import List
import random

def selection_sort(items: List[int]) -> None:
    for i in range(len(items) - 1, 0, -1):
        largest = i
        for j in range(i):
            if items[j] > items[largest]:
                largest = j
        items[i], items[largest] = items[largest], items[i]
        
# Test
items = [random.randint(1, 100) for _ in range(10)]
print("before sorting: ", *items)
selection_sort(items)
print("after sorting: ", *items)