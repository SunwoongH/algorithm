'''
문제 - 리스트 정렬

연결 리스트를 O(nlogn)에 정렬하라.

>>> O(nlogn)에 정렬하기 위해 병합 정렬 알고리즘으로 풀이하였다. 퀵 정렬로 풀이하지 않은 이유는
연결 리스트의 특성상 pivot을 원하는 형태로 설정하기 어려워 이미 정렬되거나 동일한 값이 많이 존재하는
연결 리스트가 입력으로 주어졌을 때 계속해서 최악의 형태로 리스트가 나뉘어 질 수 있기 때문이다.
아래의 풀이는 런너 방식으로 연결 리스트의 중앙값을 찾아 분할하고 분할된 각각의 연결 리스트를 오름차순으로
병합하며 해결하였다.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 내장 함수 sort() 활용 풀이 - 새로운 연결 리스트를 구축하는 방식
class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        location = head
        result = node = ListNode()
        while location:
            temp.append(location.val)
            location = location.next
        temp.sort()
        while temp:
            item = ListNode(temp.pop(), node.next)
            node.next = item
        return result.next

# 내장 함수 sort() 활용 풀이 - 기존 연결 리스트의 값을 변경하는 방식 
class Solution2:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        location = head
        temp = []
        while location:
            temp.append(location.val)
            location = location.next
        temp.sort()
        location = head
        for i in range(len(temp)):
            location.val = temp[i]
            location = location.next
        return head

# 병합 정렬 풀이 - 반복 구조로 병합하는 방식
class Solution3:
    def mergeList(self, left_head: Optional[ListNode], right_head: Optional[ListNode]) -> Optional[ListNode]:
        head = location = ListNode()
        while left_head and right_head:
            if left_head.val <= right_head.val:
                location.next, location.next.next, left_head = left_head, location.next, left_head.next
            else:
                location.next, location.next.next, right_head = right_head, location.next, right_head.next
            location = location.next
        while left_head:
            location.next, location.next.next, left_head = left_head, location.next, left_head.next
            location = location.next
        while right_head:
            location.next, location.next.next, right_head = right_head, location.next, right_head.next
            location = location.next
        return head.next
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        left_head = self.sortList(head)
        right_head = self.sortList(slow)
        return self.mergeList(left_head, right_head)

# 병합 정렬 풀이 - 재귀 구조로 병합하는 방식
class Solution4:
    def mergeList(self, left_head: Optional[ListNode], right_head: Optional[ListNode]) -> Optional[ListNode]:
        if left_head and right_head:
            if left_head.val > right_head.val:
                left_head, right_head = right_head, left_head
            left_head.next = self.mergeList(left_head.next, right_head)
        return left_head or right_head
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        left_head = self.sortList(head)
        right_head = self.sortList(slow)
        return self.mergeList(left_head, right_head)