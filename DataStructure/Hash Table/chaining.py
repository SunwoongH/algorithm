class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class Chaining:
    def __init__(self, n: int):
        self.__table = [ListNode('dummy') for _ in range(n)]
        
    def _hash_function(self, key) -> int:
        return key % len(self.__table)
    
    def search(self, key):
        hash = self._hash_function(key)
        node = self.__table[hash].next
        while node:
            if node.key == key:
                return node.value
            node = node.next
        
    def insert(self, key, value) -> None:
        hash = self._hash_function(key)
        prev, curr = self.__table[hash], self.__table[hash].next
        while curr:
            if curr.key == key:
                curr.value = value
                return
            prev, curr = curr, curr.next
        prev.next = ListNode(key, value)
        
    def delete(self, key) -> None:
        hash = self._hash_function(key)
        prev, curr = self.__table[hash], self.__table[hash].next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev, curr = curr, curr.next
            
    def __getitem__(self, key):
        return self.search(key)
    
    def __setitem__(self, key, value):
        self.insert(key, value)