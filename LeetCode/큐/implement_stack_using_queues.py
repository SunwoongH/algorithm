'''
문제 - 큐를 이용한 스택 구현

큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
 - push(x): 요소 x를 스택에 삽입한다.
 - pop(): 스택의 첫 번째 요소를 삭제한다.
 - top(): 스택의 첫 번째 요소를 가져온다.
 - empty(): 스택이 비어 있는지 여부를 반환한다.
'''
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        if self.empty():
            self.queue.append(x)
        else:
            self.queue.append(x)
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        if self.empty():
            return False
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return len(self.queue) == 0