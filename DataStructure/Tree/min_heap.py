from typing import List

class MinHeap:
    def __init__(self):
        self.__items = []
        
    def _percolate_up(self, i: int) -> None:
        parent = (i - 1) // 2
        if i > 0 and self.__items[i] < self.__items[parent]:
            self.__items[i], self.__items[parent] = self.__items[parent], self.__items[i]
            self._percolate_up(parent)
        
    def insert(self, item) -> None:
        self.__items.append(item)
        self._percolate_up(len(self.__items) - 1)
        
    def _percolate_down(self, i: int) -> None:
        child = i * 2 + 1
        if child <= len(self.__items) - 1:
            if child < len(self.__items) - 1 and self.__items[child] > self.__items[child + 1]:
                child += 1
            if self.__items[i] > self.__items[child]:
                self.__items[i], self.__items[child] = self.__items[child], self.__items[i]
                self._percolate_down(child)
        
    def delete(self):
        if self.is_empty():
            return
        removed = self.__items[0]
        self.__items[0] = self.__items[len(self.__items) - 1]
        self.__items.pop()
        self._percolate_down(0)
        return removed
    
    def is_empty(self) -> bool:
        return len(self.__items) == 0
    
    def heapify(self, items: List) -> None:
        self.__items = items[:]
        for i in range((len(self.__items) - 2) // 2, -1, -1):
            self._percolate_down(i)
    
    def print(self) -> None:
        print(*self.__items)