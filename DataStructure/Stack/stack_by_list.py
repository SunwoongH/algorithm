class Stack:
    def __init__(self):
        self.__stack = []
        
    def push(self, item) -> None:
        self.__stack.append(item)
        
    def pop(self):
        if self.is_empty():
            return
        return self.__stack.pop()
    
    def peek(self):
        if self.is_empty():
            return
        return self.__stack[-1]
    
    def is_empty(self) -> bool:
        return len(self.__stack) == 0
    
    def clear(self) -> None:
        self.__stack.clear()
        
    def print(self) -> None:
        print(*self.__stack)