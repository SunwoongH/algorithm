'''
문제 - k개 정렬 리스트 병합

k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
'''
from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 브루트 포스 풀이 - 시간 초과
class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        root = result = ListNode(None)
        root.next = None
        while True:
            check = False
            for i in range(len(lists)):
                if lists[i] is not None:
                    check = True
                    break
            if not check:
                break
            min = 0
            for i in range(1, len(lists)):
                if lists[i] is None:
                    continue
                if lists[min] is None or lists[min].val > lists[i].val:
                    min = i
            result.next = lists[min]
            result = result.next
            lists[min] = lists[min].next
        return root.next

# 우선순위 큐(heap) 풀이     
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heapq.heappop(heap)
            i = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, i, result.next))
        return root.next