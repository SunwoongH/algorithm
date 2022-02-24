class ListNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
    
    def __str__(self):
        return str(self.item)

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode('dummy')
        self.__tail.next = self.__tail
        self.__count = 0
    
    def insert(self, i: int, item) -> None:
        if i < -self.__count or i > self.__count:
            print("IndexError: insert index out of range")
            return
        if i < 0:
            i = (i + self.__count) % self.__count
        prev = self.__tail.next
        for _ in range(i):
            prev = prev.next
        new_node = ListNode(item, prev.next)
        prev.next = new_node
        if prev is self.__tail:
            self.__tail = new_node
        self.__count += 1
        
    def append(self, item) -> None:
        new_node = ListNode(item, self.__tail.next)
        self.__tail.next = new_node
        self.__tail = new_node
        self.__count += 1
        
    def pop(self, *args):
        if self.is_empty():
            print("IndexError: pop from empty list")
            return
        if not args:
            i = self.__count - 1
        elif args[0] < -self.__count or args[0] >= self.__count:
            print("IndexError: pop index out of range")
            return
        else:
            i = args[0]
            if i < 0:
                i = (i + self.__count) % self.__count
        prev = self.__tail.next
        for _ in range(i):
            prev = prev.next
        removed_item = prev.next.item
        prev.next = prev.next.next
        if i == self.__count - 1:
            self.__tail = prev
        self.__count -= 1
        return removed_item
        
    def remove(self, item) -> None:
        if self.is_empty():
            print('ValueError: list.remove(x): x not in list')
            return
        prev, node = self.__tail.next, self.__tail.next.next
        while node is not self.__tail.next:
            if node.item == item:
                prev.next = node.next
                if node is self.__tail:
                    self.__tail = prev
                self.__count -= 1
                return
            prev, node = node, node.next
        print('ValueError: list.remove(x): x not in list')

    def get(self, i: int):
        if i < -self.__count or i >= self.__count:
            print("IndexError: get index out of range")
            return
        if i < 0:
            i = (i + self.__count) % self.__count
        node = self.__tail.next.next
        for _ in range(i):
            node = node.next
        return node.item

    def index(self, item) -> int:
        if self.is_empty():
            print(f"ValueError: {item} is not in list")
            return -1
        i = 0
        node = self.__tail.next.next
        while node is not self.__tail.next:
            if node.item == item:
                return i
            node, i = node.next, i + 1
        print(f"ValueError: {item} is not in list")
        return -1
    
    def is_empty(self) -> bool:
        return self.__count == 0
    
    def size(self) -> int:
        return self.__count
    
    def clear(self) -> None:
        self.__tail = ListNode('dummy')
        self.__tail.next = self.__tail
        self.__count = 0
        
    def count(self, item) -> int:
        count = 0
        node = self.__tail.next.next
        while node is not self.__tail.next:
            if node.item == item:
                count +=1
            node = node.next
        return count
            
    def extend(self, iterable_object) -> None:
        for element in iterable_object:
            self.append(element)
    
    def copy(self) -> 'CircularLinkedList':
        new_linked_list = CircularLinkedList()
        for element in self:
            new_linked_list.append(element.item)
        return new_linked_list

    def reverse(self) -> None:
        prev, node, dummy_node = self.__tail.next, self.__tail.next.next, self.__tail.next
        self.__tail = node
        while node is not dummy_node:
            node.next, prev, node = prev, node, node.next
        dummy_node.next = prev
    
    def sort(self, reverse=False) -> None:
        temp = []
        for element in self:
            temp.append(element.item)
        temp.sort(reverse=reverse)
        self.clear()
        for element in temp:
            self.append(element)
            
    def __iter__(self):
        node = self.__tail.next.next
        while node is not self.__tail.next:
            yield node
            node = node.next
        
    def __str__(self):
        return "->".join(str(node) for node in self)