import sys
MAX_DATA_SIZE = 2000000

class Queue:
    def __init__(self):
        self.data = [0] * MAX_DATA_SIZE
        self.front = 0
        self.rear = 0
    def isFull(self):
        if self.front == (self.rear + 1) % MAX_DATA_SIZE: return 1
        else: return 0
    def isEmpty(self):
        if self.front == self.rear: return 1
        else: return 0
    def enqueue(self, key):
        if self.isFull(): return
        self.rear = (self.rear + 1) % MAX_DATA_SIZE
        self.data[self.rear] = key
    def dequeue(self):
        if self.isEmpty(): return -1
        self.front = (self.front + 1) % MAX_DATA_SIZE
        return self.data[self.front]
    def count(self):
        return self.rear - self.front
    def peekFront(self):
        if self.isEmpty(): return -1
        return self.data[(self.front + 1) % MAX_DATA_SIZE]
    def peekBack(self):
        if self.isEmpty(): return -1
        return self.data[self.rear]

n = int(sys.stdin.readline())
queue = Queue()
for i in range(n):
    order = sys.stdin.readline().strip('\n')
    if order[:4] == 'push':
        queue.enqueue(int(order[5:]))
    else:
        if order == 'pop':
            print(queue.dequeue())
        elif order == 'size':
            print(queue.count())
        elif order == 'empty':
            print(queue.isEmpty())
        elif order == 'front':
            print(queue.peekFront())
        elif order == 'back':
            print(queue.peekBack())