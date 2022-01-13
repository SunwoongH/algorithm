'''
문제 - 홀짝 연결 리스트

연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.
공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, temp = head, head.next
        even = temp_even = ListNode(None)
        while temp and temp.next:
            prev.next = temp.next
            temp_even.next = temp
            temp_even = temp_even.next
            temp = temp.next.next
            prev = prev.next
        if temp:
            temp_even.next = temp
            temp_even = temp_even.next
        temp_even.next = None
        prev.next = even.next
        return head
    
class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd = head
        even_head = even = head.next
        while even and even.next:
            # odd.next, odd = odd.next.next, odd.next.next
            # even.next, even = even.next.next, even.next.next
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head