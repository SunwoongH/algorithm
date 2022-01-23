'''
문제 - 정렬된 배열의 이진 탐색 트리 변환

오름차순으로 정렬된 배열을 높이 균형(Height Balanced) 이진 탐색 트리로 변환하라.
'''
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# AVL 트리 풀이 - 시간 초과
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = None
        def _height(node):
            if not node:
                return 0
            left = _height(node.left)
            right = _height(node.right)
            return 1 + max(left, right)
        def _left_rotate(node):
            child = node.right
            child.left, node.right = node, child.left
            return child
        def _right_rotate(node):
            child = node.left
            child.right, node.left = node, child.right
            return child
        def _rebalance(node):
            balance_factor = _height(node.left) - _height(node.right)
            if balance_factor > 1:
                if _height(node.left.left) - _height(node.left.right) < 0:
                    node.left = _left_rotate(node.left)
                return _right_rotate(node)
            elif balance_factor < -1:
                if _height(node.right.left) - _height(node.right.right) > 0:
                    node.left = _right_rotate(node.left)
                return _left_rotate(node)
            return node
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val == node.val:
                return node
            elif val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return _rebalance(node)
        for num in nums:
            root = _insert(root, num)
        return root

# DFS(재귀)와 이진 탐색의 특징을 적용한 풀이
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(mid)
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node