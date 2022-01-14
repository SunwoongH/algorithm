'''
문제 - 원형 덱 디자인

다음 연산을 제공하는 원형 덱을 디자인하라.

MyCircularDeque(k) - k 사이즈의 덱을 생성.
insertFront() - 덱 처음에 아이템을 추가하고 성공할 경우 true 반환.
insertLast() - 덱 마지막에 아이템을 추가하고 성공할 경우 true 반환.
deleteFront() - 덱 처음에 아이템을 삭제하고 성공할 경우 true 반환.
deleteLast() - 덱 마지막에 아이템을 삭제하고 성공할 경우 true 반환.
getFront() - 덱의 첫 번째 아이템을 가져온다. 덱이 비어있으면 -1 반환.
getRear() - 덱의 마지막 아이템을 가져온다. 덱이 비어있으면 -1 반환.
isEmpty() - 덱이 비어있는지 여부를 판별.
isFull() - 덱이 가득차 있는지 여부를 판별.
'''

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 리스트 풀이
class MyCircularDeque1:
    def __init__(self, k: int):
        self.size = k
        self.item = [None] * self.size
        self.front = 0
        self.rear = 0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.item[self.front] = value
        self.front = (self.front - 1 + self.size) % self.size
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.item[self.rear] = value
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.item[self.front] = None
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.item[self.rear] = None
        self.rear = (self.rear - 1 + self.size) % self.size
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.item[(self.front + 1) % self.size]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.item[self.rear]    
    def isEmpty(self) -> bool:
        return self.front == self.rear and self.item[self.front] is None
    def isFull(self) -> bool:
        return self.front == self.rear and self.item[self.front] is not None

# 이중 연결 리스트 풀이
class MyCircularDeque2:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
    def _add(self, node: ListNode, new_node: ListNode):
        temp = node.right
        node.right = new_node
        new_node.left, new_node.right = node, temp
        temp.left = new_node
        
        # 다중 할당 - 첫 번째 변수 부터 할당.
        #new_node.left, new_node.right = node, node.right
        #node.right.left = node.right = new_node
        
        # 다중 할당 - 우변 값 선 평가 후 좌변 변수 순서대로 할당.
        #new_node.left, new_node.right = node, node.right
        #node.right.left, node.right = new_node, new_node
        
    def _del(self, node: ListNode):
        remove = node.right
        node.right = remove.right
        remove.right.left = node
        del remove
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.head)
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    def getFront(self) -> int:
        return self.head.right.val if not self.isEmpty() else -1
    def getRear(self) -> int:
        return self.tail.left.val if not self.isEmpty() else -1
    def isEmpty(self) -> bool:
        return self.len == 0
    def isFull(self) -> bool:
        return self.len == self.k