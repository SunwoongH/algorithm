'''
문제 - 중위, 후위 순회 결과로 이진 트리 구축

트리의 중위, 후위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.
'''
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Divide and Conquer 풀이
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            i = inorder.index(postorder.pop())
            node = TreeNode(inorder[i])
            node.right = self.buildTree(inorder[i + 1:], postorder)
            node.left = self.buildTree(inorder[:i], postorder)
            return node