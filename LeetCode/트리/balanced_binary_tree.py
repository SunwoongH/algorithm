'''
문제 - 균형 이진 트리

이진 트리가 높이 균형(Height - Balanced)인지 판단하라.

높이 균형(Height - Balanced): 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것.
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS(재귀) 풀이
class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if self.balanced and abs(left - right) > 1:
                self.balanced = False
            return max(left, right) + 1
        dfs(root)
        return self.balanced

# DFS(재귀) 풀이
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1