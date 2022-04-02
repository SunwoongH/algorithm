'''
Created by sunwoong on 2022/04/02
'''
import sys
import collections

class Queue:
    def __init__(self):
        self.__queue = collections.deque()
    
    def push(self, item: int) -> None:
        self.__queue.append(item)
    
    def pop(self) -> int:
        if self.is_empty():
            return -1
        return self.__queue.popleft()
    
    def size(self) -> int:
        return len(self.__queue)
    
    def is_empty(self) -> int:
        return len(self.__queue) == 0
    
    def peek_front(self) -> int:
        if self.is_empty():
            return -1
        return self.__queue[0]
    
    def peek_back(self) -> int:
        if self.is_empty():
            return -1
        return self.__queue[-1]
    
n = int(sys.stdin.readline())
queue = Queue()
for _ in range(n):
    order = sys.stdin.readline().rstrip('\n')
    if order[:4] == 'push':
        queue.push(int(order[5:]))
    elif order == 'pop':
        print(queue.pop())
    elif order == 'size':
        print(queue.size())
    elif order == 'empty':
        print(1 if queue.is_empty() == True else 0)
    elif order == 'front':
        print(queue.peek_front())
    else:
        print(queue.peek_back())