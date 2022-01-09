'''
문제 - 원형 큐 디자인

원형 큐를 디자인하라.
'''

class MyCircularQueue1:
    def __init__(self, k: int):
        self.queue = [0] * (k + 1)
        self.size = k + 1
        self.front = 0
        self.rear = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.front + 1) % self.size]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    def isEmpty(self) -> bool:
        return self.front == self.rear
    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
    
class MyCircularQueue2:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.front = 0
        self.rear = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True
    def Front(self) -> int:
        return -1 if self.queue[self.front] is None else self.queue[self.front]
    def Rear(self) -> int:
        return -1 if self.queue[self.rear - 1] is None else self.queue[self.rear - 1]
    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None
    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None