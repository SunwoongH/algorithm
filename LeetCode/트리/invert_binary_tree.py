'''
문제 - 이진 트리 반전

이진 트리를 반전시켜라.

>>> 구글 입사 면접에 나왔다고 한다. 재귀적으로 접근해서 문제를 해결할 수 있는 직관을 기르도록 노력하자.
'''
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS(재귀) 풀이
class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        '''
        >>> 파이썬의 다중 할당은 아래 코드와 동일한 역할을 한다.
        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        '''
        return root

# BFS 풀이
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.right, node.left = node.left, node.right
                queue.append(node.left)
                queue.append(node.right)
        return root

# DFS(반복) 풀이 - preorder
class Solution3:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                stack.append(node.left)
                stack.append(node.right)
        return root

# DFS(반복) 풀이 - postorder
class Solution4:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.right, node.left = node.left, node.right
        return root