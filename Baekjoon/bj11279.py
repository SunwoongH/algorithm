'''
문제 - 최대 힙

풀이 방법 - 재귀적으로 힙 특성을 재구축하는 함수를 구현하여 최대 힙 설계
'''
import sys

class Heap:
    def __init__(self):
        self.__items = []
        
    def __percolate_up(self, i: int) -> None:
        parent = (i - 1) // 2
        if i > 0 and self.__items[i] > self.__items[parent]:
            self.__items[i], self.__items[parent] = self.__items[parent], self.__items[i]
            self.__percolate_up(parent)
    
    def insert(self, item) -> None:
        self.__items.append(item)
        self.__percolate_up(len(self.__items) - 1)
        
    def __percolate_down(self, i: int) -> None:
        child = i * 2 + 1
        if child <= len(self.__items) - 1:
            if child < len(self.__items) - 1 and self.__items[child] < self.__items[child + 1]:
                child += 1
            if self.__items[i] < self.__items[child]:
                self.__items[i], self.__items[child] = self.__items[child], self.__items[i]
                self.__percolate_down(child)
        
    def delete(self):
        if self.is_empty():
            return 0
        removed = self.__items[0]
        self.__items[0] = self.__items[len(self.__items) - 1]
        self.__items.pop()
        self.__percolate_down(0)
        return removed
    
    def is_empty(self) -> bool:
        return len(self.__items) == 0
    
n = int(sys.stdin.readline())
heap = Heap()
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0: print(heap.delete())
    else: heap.insert(x)