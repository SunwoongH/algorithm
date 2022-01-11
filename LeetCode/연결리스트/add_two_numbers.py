'''
문제 - 두 수의 덧셈

역순으로 저장된 연결 리스트의 숫자를 더하라.
'''
from typing import Optional, List
import functools

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        num1, num2 = [], []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        num1 = int(''.join(num1[::-1]))
        num2 = int(''.join(num2[::-1]))
        temp = list(str(num1 + num2))
        for num in temp:
            num_temp = ListNode(num)
            result, result.next = num_temp, result
        return result
    
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node is not None:
            list.append(node.val)
            node = node.next
        return list
    
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for num in result:
            node = ListNode(int(num))
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        result_str = int(''.join(str(num) for num in a)) + \
                     int(''.join(str(num) for num in b))

        #result_str = int(''.join(map(str, a))) + \
        #             int(''.join(map(str, b)))
                     
        #result_str = functools.reduce(lambda x, y: 10 * x + y, a) + \
        #             functools.reduce(lambda x, y: 10 * x + y, b)
        
        return self.toReversedLinkedList(str(result_str))