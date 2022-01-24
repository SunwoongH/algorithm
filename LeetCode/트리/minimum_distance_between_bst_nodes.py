'''
문제 - 이진 탐색 트리 노드 간 최소 거리

두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
'''
from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution1:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.pre_value = -1
        self.result = sys.maxsize
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                if self.pre_value == -1:
                    self.pre_value = node.val
                else:
                    if node.val - self.pre_value < self.result:
                        self.result = node.val - self.pre_value
                    self.pre_value = node.val
                inorder(node.right)
        inorder(root)
        return self.result

# DFS(재귀) inorder 풀이
class Solution2:
    prev: int = -sys.maxsize
    result: int = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.result

# DFS(반복) inorder 풀이
class Solution3:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val
            node = node.right
        return result