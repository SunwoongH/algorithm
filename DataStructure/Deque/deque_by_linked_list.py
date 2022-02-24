class DequeNode:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.item)
    
class Deque:
    def __init__(self):
        self.__front = DequeNode('dummy')
        self.__rear = DequeNode('dummy')
        self.__front.next, self.__rear.prev = self.__rear, self.__front
        self.__size = 0
        
    def append_left(self, item) -> None:
        new_node = DequeNode(item, self.__front, self.__front.next)
        new_node.next.prev = new_node
        self.__front.next = new_node
        self.__size += 1
        
    def append(self, item) -> None:
        new_node = DequeNode(item, self.__rear.prev, self.__rear)
        new_node.prev.next = new_node
        self.__rear.prev = new_node
        self.__size += 1
        
    def pop_left(self):
        if self.is_empty():
            return
        removed = self.__front.next
        removed_item = removed.item
        self.__front.next = removed.next
        removed.next.prev = self.__front
        self.__size -= 1
        return removed_item
        
    def pop(self):
        if self.is_empty():
            return
        removed = self.__rear.prev
        removed_item = removed.item
        self.__rear.prev = removed.prev
        removed.prev.next = self.__rear
        self.__size -= 1
        return removed_item
    
    def peek_front(self):
        if self.is_empty():
            return
        return self.__front.next.item
    
    def peek_rear(self):
        if self.is_empty():
            return
        return self.__rear.prev.item
    
    def is_empty(self) -> bool:
        return self.__size == 0
    
    def size(self) -> int:
        return self.__size
    
    def __iter__(self):
        node = self.__front.next
        while node is not self.__rear:
            yield node
            node = node.next
            
    def __str__(self):
        return '->'.join(str(node) for node in self)