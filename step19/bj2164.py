import sys

class Queue:
    def __init__(self, n):
        self.data = [0]
        for i in range(n):
            self.data.append(i + 1)
        self.front = 0
        self.rear = n
    def isFull(self):
        return self.front == (self.rear + 1) % (n + 1)
    def isEmpty(self):
        return self.front == self.rear
    def enqueue(self, key):
        if self.isFull(): return False
        self.rear = (self.rear + 1) % (n + 1)
        self.data[self.rear] = key
    def dequeue(self):
        if self.isEmpty(): return False
        self.front = (self.front + 1) % (n + 1)
        return self.data[self.front]
    def count(self):
        return self.rear == (self.front + 1) % (n + 1)
    def peekFront(self):
        if self.isEmpty(): return False
        return self.data[(self.front + 1) % (n + 1)]

n = int(sys.stdin.readline())
card = Queue(n)
while True:
    if card.count() == True: break
    card.dequeue()
    card.enqueue(card.dequeue())
print(card.peekFront())