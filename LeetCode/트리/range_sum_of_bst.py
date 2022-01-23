'''
문제 - 이진 탐색 트리 합의 범위

이진 탐색 트리가 주어졌을 때 low 이상 high 이하의 값을 지닌 노드의 합을 구하라.
'''
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution1:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        def _inorder(node: TreeNode):
            if node:
                _inorder(node.left)
                if node.val >= low and node.val <= high:
                    self.result += node.val
                _inorder(node.right)
        _inorder(root)
        return self.result

# DFS(재귀) 브루트 포스 풀이
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return None
        return (root.val if root.val >= low and root.val <= high else 0) \
            + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# DFS(재귀) pruning 풀이   
class Solution3:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)

# DFS(반복) 풀이
class Solution4:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, result = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if node.val >= low and node.val <= high:
                    result += node.val
        return result

# BFS 풀이
class Solution5:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue, result = collections.deque([root]), 0
        while queue:
            node = queue.popleft()
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if node.val >= low and node.val <= high:
                    result += node.val
        return result