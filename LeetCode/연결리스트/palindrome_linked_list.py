'''
문제 - 팰린드롬 연결 리스트

연결 리스트가 팰린드롬 구조인지 판별하라.
'''
from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 슬라이싱 풀이
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False 
        test = []
        node = head
        while node != None:
            test.append(node.val)
            node = node.next
        return test == test[::-1]

# 리스트 풀이
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        test = []
        node = head
        while node != None:
            test.append(node.val)
            node = node.next
        while len(test) > 1:
            if test.pop(0) != test.pop():
                return False
        return True

# 덱 풀이
class Solution3:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        test = deque()
        node = head
        while node != None:
            test.append(node.val)
            node = node.next
        while len(test) > 1:
            if test.popleft() != test.pop():
                return False
        return True

# 런너 기법 풀이
class Solution4:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev