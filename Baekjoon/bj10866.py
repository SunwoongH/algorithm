'''
문제 - 덱

풀이 방법 - front, rear 더미 노드 포인터를 활용한 단순 연결 리스트로 구현
'''
import sys

class DequeNode:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next
        
class Deque:
    def __init__(self):
        self.__front = DequeNode('dummy')
        self.__rear = DequeNode('dummy')
        self.__front.next, self.__rear.prev = self.__rear, self.__front
        self.__size = 0
        
    def append_left(self, item: int) -> None:
        new_node = DequeNode(item, self.__front, self.__front.next)
        new_node.next.prev = new_node
        self.__front.next = new_node
        self.__size += 1
        
    def append(self, item: int) -> None:
        new_node = DequeNode(item, self.__rear.prev, self.__rear)
        new_node.prev.next = new_node
        self.__rear.prev = new_node
        self.__size += 1
        
    def pop_left(self) -> int:
        if self.is_empty() == 1:
            return -1
        removed = self.__front.next
        removed_item = removed.item
        self.__front.next = removed.next
        removed.next.prev = self.__front
        self.__size -= 1
        return removed_item
        
    def pop(self) -> int:
        if self.is_empty() == 1:
            return -1
        removed = self.__rear.prev
        removed_item = removed.item
        self.__rear.prev = removed.prev
        removed.prev.next = self.__rear
        self.__size -= 1
        return removed_item
    
    def peek_front(self) -> int:
        if self.is_empty() == 1:
            return -1
        return self.__front.next.item
    
    def peek_rear(self) -> int:
        if self.is_empty() == 1:
            return -1
        return self.__rear.prev.item
    
    def is_empty(self) -> int:
        return 1 if self.__size == 0 else 0
    
    def size(self) -> int:
        return self.__size
    
n = int(sys.stdin.readline())
deque = Deque()
order = {'size': deque.size, 'empty': deque.is_empty, \
         'front': deque.peek_front, 'back': deque.peek_rear}
for _ in range(n):
    input_order = sys.stdin.readline().strip('\n')
    if input_order[:4] == 'push':
        if input_order[5:10] == 'front':
            deque.append_left(int(input_order[11:]))
        else:
            deque.append(int(input_order[10:]))
    elif input_order[:3] == 'pop':
        if input_order[4:] == 'front':
            print(deque.pop_left())
        else:
            print(deque.pop())
    else:
        print(order[input_order]())