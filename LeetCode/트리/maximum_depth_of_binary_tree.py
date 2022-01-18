'''
문제 - 이진 트리의 최대 깊이

이진 트리의 최대 깊이를 구하라.
'''
from typing import Optional
import collections, math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS 풀이
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = []
        def dfs(node, depth):
            if not node.left and not node.right:
                result.append(depth)
                return
            else:
                if node.left:
                    dfs(node.left, depth + 1)
                if node.right:
                    dfs(node.right, depth + 1)
        dfs(root, 1)
        return max(result)

# BFS 풀이
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth