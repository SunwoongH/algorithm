import sys

class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def insertMinHeap(self, key):
        self.heap.append(key)
        self.size += 1
        i = self.size

        while i != 1 and key < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            i //= 2
        self.heap[i] = key

    def deleteMinHeap(self):
        if self.isEmpty():
            return False
        removed = self.heap[1]
        tempKey = self.heap[self.size]
        self.size -= 1
        parent = 1
        child = 2

        while child <= self.size:
            if (child < self.size) and (self.heap[child] > self.heap[child + 1]):
                child += 1
            if tempKey <= self.heap[child]: break
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2
        self.heap[parent] = tempKey
        return removed

heap = Heap()
N = int(sys.stdin.readline())
for i in range(0, N):
    num = int(sys.stdin.readline())
    if num == 0:
        minV = heap.deleteMinHeap()
        if minV == False:
            print(0)
        else:
            print(minV)
    else:
        heap.insertMinHeap(num)

