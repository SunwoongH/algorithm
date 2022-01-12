'''
문제 - 페어의 노드 스왑

연결 리스트를 입력받아 pair 단위로 swap하라.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd, even = None, None
        node = head
        count = 1
        odd_count, even_count = 0, 0
        while node is not None:
            if count % 2 != 0:
                odd, odd.next, node = node, odd, node.next
                odd_count += 1
            else:
                even, even.next, node = node, even, node.next
                even_count += 1
            count += 1
        result = None
        count = 1
        if odd_count > even_count:
            result, result.next, odd = odd, result, odd.next
        while odd or even:
            if count % 2 != 0:
                result, result.next, odd = odd, result, odd.next
            else:
                result, result.next, even = even, result, even.next
            count += 1
        return result

# node를 swap하지 않고 node의 값을 swap한 풀이
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

# 반복구조 풀이
class Solution3:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            prev.next = temp
            head = head.next
            prev = prev.next.next
        return root.next

# 재귀구조 풀이
class Solution4:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head