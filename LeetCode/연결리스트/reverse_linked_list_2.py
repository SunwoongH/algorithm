'''
문제 - 역순 연결 리스트

인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        prev_node, next_node = None, None
        temp = head
        temp_node = None
        count = 1
        while temp:
            if count < left:
                if prev_node is None:
                    prev_node = temp
                else:
                    prev_node.next = temp
                    prev_node = prev_node.next
                temp = temp.next
            elif count >= left and count <= right:
                item = temp
                item.next, temp = temp_node, temp.next
                temp_node = item
            elif count == right + 1:
                next_node = temp
                temp = temp.next
            else:
                temp = temp.next
            count += 1
        t = temp_node
        while t.next:
            t = t.next
        t.next = next_node
        if prev_node is None:
            return temp_node
        else:
            prev_node.next = temp_node
            return head
        
class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or right == left:
            return head
        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        return root.next