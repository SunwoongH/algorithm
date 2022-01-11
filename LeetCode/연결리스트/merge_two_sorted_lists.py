'''
문제 - 두 정렬 리스트의 병합

정렬되어 있는 두 연결 리스트를 합쳐라.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        if list1 and list2:
            if list1.val <= list2.val:
                result, result.next, list1 = list1, result, list1.next
            else:
                result, result.next, list2 = list2, result, list2.next
        while list1 and list2:
            temp = result
            while temp.next is not None:
                temp = temp.next
            if list1.val <= list2.val:
                temp.next, temp.next.next, list1 = list1, None, list1.next
            else:
                temp.next, temp.next.next, list2 = list2, None, list2.next
        if list1:
            while list1:
                if result is None:
                    result, result.next, list1 = list1, None, list1.next
                else:
                    temp = result
                    while temp.next is not None:
                        temp = temp.next
                    temp.next, temp.next.next, list1 = list1, None, list1.next
        elif list2:
            while list2:
                if result is None:
                    result, result.next, list2 = list2, None, list2.next
                else:
                    temp = result
                    while temp.next is not None:
                        temp = temp.next
                    temp.next, temp.next.next, list2 = list2, None, list2.next
        return result

# 재귀구조 풀이
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1