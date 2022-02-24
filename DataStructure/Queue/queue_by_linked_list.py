class QueueNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
    
class Queue:
    def __init__(self):
        self.__front = self.__tail = QueueNode('dummy')
        
    def enqueue(self, item) -> None:
        new_node = QueueNode(item)
        self.__tail.next = new_node
        self.__tail = new_node
        
    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        removed_item = self.__front.next.item
        self.__front.next = self.__front.next.next
        if self.__front.next is None:
            self.__tail = self.__front
        return removed_item
        
    def front(self):
        if self.is_empty():
            print('queue is empty')
            return
        return self.__front.next.item
    
    def is_empty(self) -> bool:
        return self.__front is self.__tail

    def clear(self) -> None:
        self.__front = self.__tail = QueueNode('dummy')