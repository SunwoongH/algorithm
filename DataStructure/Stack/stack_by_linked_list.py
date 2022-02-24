class StackNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self):
        self.__head = StackNode('dummy')

    def push(self, item) -> None:
        new_node = StackNode(item, self.__head.next)
        self.__head.next = new_node
    
    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return
        removed_item = self.__head.next.item
        self.__head.next = self.__head.next.next
        return removed_item
    
    def peek(self):
        if self.is_empty():
            print('stack is empty')
            return
        return self.__head.next.item
        
    def is_empty(self) -> bool:
        return self.__head.next is None
    
    def clear(self) -> None:
        self.__head = StackNode('dummy')