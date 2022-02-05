import sys

class Deque:
    def __init__(self, n):
        self.size = n + 1
        self.data = [0] * self.size
        self.front = 0
        self.rear = 0
    def isEmpty(self):
        if self.front == self.rear: return 1
        else: return 0
    def pushFront(self, key):
        self.data[self.front] = key
        self.front = (self.front - 1 + self.size) % self.size
    def pushBack(self, key):
        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = key
    def popFront(self):
        if self.isEmpty(): return -1
        self.front = (self.front + 1) % self.size
        return self.data[self.front]
    def popBack(self):
        if self.isEmpty(): return -1
        removed = self.data[self.rear]
        self.rear = (self.rear - 1 + self.size) % self.size
        return removed
    def peekFront(self):
        if self.isEmpty(): return -1
        return self.data[(self.front + 1) % self.size]
    def peekBack(self):
        if self.isEmpty(): return -1
        return self.data[self.rear]
    def sizeD(self):
        if self.isEmpty(): return 0
        temp = self.rear
        count = 0
        while temp != self.front:
            count += 1
            temp = (temp - 1 + self.size) % self.size
        return count

n = int(sys.stdin.readline())
deque = Deque(n)
for i in range(n):
    order = sys.stdin.readline().strip('\n')
    if order[:9] == 'push_back':
        deque.pushBack(int(order[9:]))
    elif order[:10] == 'push_front':
        deque.pushFront(int(order[10:]))
    elif order == 'pop_front':
        print(deque.popFront())
    elif order == 'pop_back':
        print(deque.popBack())
    elif order == 'size':
        print(deque.sizeD())
    elif order == 'empty':
        print(deque.isEmpty())
    elif order == 'front':
        print(deque.peekFront())
    elif order == 'back':
        print(deque.peekBack())