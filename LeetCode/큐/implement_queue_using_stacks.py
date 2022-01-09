'''
문제 - 스택을 이용한 큐 구현

스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
 - push(x): 요소 x를 큐 마지막에 삽입한다.
 - pop(): 큐 처음에 있는 요소를 제거한다.
 - top(): 큐 처음에 있는 요소를 조회한다.
 - empty(): 큐가 비어 있는지 여부를 반환한다.
'''

class MyQueue1:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        temp = []
        if self.empty():
            self.stack.append(x)
        else:
            while self.stack:
                temp.append(self.stack.pop())
            self.stack.append(x)
            while temp:
                self.stack.append(temp.pop())
    def pop(self) -> int:
        if self.empty():
            return False
        return self.stack.pop()
    def peek(self) -> int:
        if self.empty():
            return False
        return self.stack[-1]
    def empty(self) -> bool:
        return len(self.stack) == 0

class MyQueue2:
    def __init__(self):
        self.input = []
        self.output = []
    def push(self, x: int) -> None:
        self.input.append(x)
    def pop(self) -> int:
        self.peek()
        return self.output.pop()
    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    def empty(self) -> bool:
        return self.input == [] and self.output == []