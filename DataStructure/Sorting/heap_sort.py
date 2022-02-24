from typing import List
import random

def percolate_down(items: List[int], i: int, size: int) -> None:
    child = i * 2 + 1
    if child <= size - 1:
        if child < size - 1 and items[child] < items[child + 1]:
            child += 1
        if items[i] < items[child]:
            items[i], items[child] = items[child], items[i]
            percolate_down(items, child, size)
            
def heapify(items: List[int]) -> None:
    for i in range((len(items) - 2) // 2, -1, -1):
        percolate_down(items, i, len(items))

def heap_sort(items: List[int]) -> None:
    heapify(items)
    for i in range(len(items) - 1, 0, -1):
        items[i], items[0] = items[0], items[i]
        percolate_down(items, 0, i)
        
# Test
items = [random.randint(1, 100) for _ in range(10)]
print("before sorting: ", *items)
heap_sort(items)
print("after sorting: ", *items)