'''
문제 - 해시맵 디자인

다음의 기능을 제공하는 해시맵을 디자인하라.

put(key, value): (키, 값)을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
get(key): 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 반환한다.
remove(key): 키에 해당하는 (키, 값)을 해시맵에서 삭제한다.
'''
import collections

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

# 리스트 체이닝 풀이
class MyHashMap1:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size
    
    def hash_function(self, key):
        return key % self.size

    def hashing(self, key):
        return self.hash_function(key)

    def put(self, key: int, value: int) -> None:
        i = self.hashing(key)
        if self.table[i] is None:
            self.table[i] = Node(key, value)
        else:
            temp = self.table[i]
            while temp:
                if temp.key == key:
                    temp.value = value
                    return
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = Node(key, value)
            
    def get(self, key: int) -> int:
        i = self.hashing(key)
        temp = self.table[i]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return -1

    def remove(self, key: int) -> None:
        i = self.hashing(key)
        if self.table[i] is None:
            return
        else:
            prev, remove = None, self.table[i]
            while remove:
                if remove.key == key:
                    break
                prev, remove = remove, remove.next
            if remove is None:
                return
            if prev is None:
                self.table[i] = remove.next
            else:
                prev.next = remove.next
            del remove

# 딕셔너리 체이닝 풀이
class MyHashMap2:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(Node)
        
    def put(self, key: int, value: int) -> None:
        i = key % self.size
        if self.table[i].value is None:
            self.table[i] = Node(key, value)
            return
        temp = self.table[i]
        while temp:
            if temp.key == key:
                temp.value = value
                return
            if temp.next is None:
                break
            temp = temp.next
        temp.next = Node(key, value)
            
    def get(self, key: int) -> int:
        i = key % self.size
        if self.table[i].value is None:
            return -1
        temp = self.table[i]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return -1

    def remove(self, key: int) -> None:
        i = key % self.size
        if self.table[i].value is None:
            return
        temp = self.table[i]
        if temp.key == key:
            self.table[i] = Node() if temp.next is None else temp.next
            return
        prev = None
        while temp:
            if temp.key == key:
                prev.next = temp.next
                return
            prev, temp = temp, temp.next     