import sys

class PriorityQueue:
    def __init__(self, n):
        self.queue = [0] * (n + 1)
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def insert(self, num):
        self.size += 1
        i = self.size
        while i > 1 and abs(num) <= abs(self.queue[i // 2]):
            if abs(num) == abs(self.queue[i // 2]):
                if num < self.queue[i // 2]:
                    self.queue[i] = self.queue[i // 2]
                    i //= 2
                else: break
            else:
                self.queue[i] = self.queue[i // 2]
                i //= 2
        self.queue[i] = num
    def delete(self):
        if self.is_empty(): return 0
        removed = self.queue[1]
        temp = self.queue[self.size]
        self.size -= 1
        parent = 1
        child = 2
        while self.size >= child:
            if self.size > child and abs(self.queue[child]) > abs(self.queue[child + 1]): child += 1
            elif self.size > child and abs(self.queue[child]) == abs(self.queue[child + 1]):
                if self.queue[child] > self.queue[child + 1]: child += 1
            if abs(temp) < abs(self.queue[child]): break
            elif abs(temp) == abs(self.queue[child]):
                if temp < self.queue[child]: break
            self.queue[parent] = self.queue[child]
            parent = child
            child *= 2
        self.queue[parent] = temp
        return removed
    
n = int(sys.stdin.readline())
heap = PriorityQueue(n)
for _ in range(n):
    input_data = int(sys.stdin.readline())
    if input_data == 0: print(heap.delete())
    else: heap.insert(input_data)