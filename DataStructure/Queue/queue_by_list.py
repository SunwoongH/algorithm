class Queue:
    def __init__(self):
        self.__queue = []
        
    def enqueue(self, item) -> None:
        self.__queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            print('queue is empty')
            return
        return self.__queue[0]

    def is_empty(self) -> bool:
        return len(self.__queue) == 0
    
    def clear(self) -> None:
        self.__queue.clear()