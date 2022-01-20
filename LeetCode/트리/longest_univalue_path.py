'''
문제 - 가장 긴 동일 값의 경로

동일한 값을 지닌 가장 긴 경로를 찾아라.
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS 풀이
class Solution:
    distance: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            self.distance = max(self.distance, left + right)
            return max(left, right)
        dfs(root)
        return self.distance