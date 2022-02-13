'''
문제 - 삽입 정렬 리스트

연결 리스트를 삽입 정렬로 정렬하라.

>>> 주어진 연결 리스트는 단일 연결 리스트로 이미 지나왔던 노드로 다시 돌아갈 수 없는 특징을 가지고 있다.
따라서 오른쪽 노드에서 왼쪽 노드로 진행하며 값 비교를 하는 삽입 정렬의 특징을 구현하기는 불가능하다. 따라서
이 문제에서는 왼쪽 노드에서 오른쪽 노드로 진행하도록 구현하였다. 다만 이와 같은 연산은 매번 가장 작은 값 
즉, 제일 왼쪽 노드에서 시작해 차례대로 크기 비교를 진행하기 때문에 비효율적이다. 이러한 비효율적인 연산을 
개선하고자 마지막 노드의 값과 다음 검사해야할 노드의 값을 비교해 되돌아가지 않아도 되는 경우를 추가 조건으로 
설정하여 풀이하였다.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 연결 리스트를 직접 정렬하는 풀이
class Solution1:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, node = head, head.next
        prev, curr = None, head
        while node:
            while curr is not node and curr.val <= node.val:
                prev, curr = curr, curr.next
            if curr is node:
                prev_node, node = node, node.next
            elif not prev:
                head, node.next, node = node, curr, node.next
                prev_node.next = node
            else:
                prev.next, node.next, node = node, curr, node.next
                prev_node.next = node
            # 최적화 조건 추가 설정
            if node and curr.val > node.val:
                prev, curr = None, head
        return head

# 새로운 연결 리스트를 만들어 정렬하는 풀이
class Solution2:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = parent = ListNode()
        while head:
            while curr.next and curr.next.val <= head.val:
                curr = curr.next
            curr.next, head.next, head = head, curr.next, head.next
            curr = parent
        return parent.next

# 새로운 연결 리스트를 만들어 정렬하는 풀이 - 최적화
class Solution3:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = parent = ListNode()
        while head:
            while curr.next and curr.next.val <= head.val:
                curr = curr.next
            curr.next, head.next, head = head, curr.next, head.next
            # 최적화 조건 추가 설정
            if head and curr.next.val > head.val:
                curr = parent
        return parent.next