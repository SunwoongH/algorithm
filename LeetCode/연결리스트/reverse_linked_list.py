'''
문제 - 역순 연결 리스트

연결 리스트를 뒤집어라.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 반복구조 풀이
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        temp = head
        while temp is not None:
            rev, rev.next, temp = temp, rev, temp.next
        return rev

# 재귀구조 풀이
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)

# 반복구조 풀이
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev