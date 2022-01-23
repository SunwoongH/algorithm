'''
문제 - 이진 탐색 트리를 더 큰 수 합계 트리로 만들기

이진 탐색 트리의 각 노드의 값을 현재값과 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS(재귀) inorder(right -> node -> left)로 value 누적 풀이
class Solution:
    sum_of_val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.bstToGst(root.right)
        self.sum_of_val += root.val
        root.val = self.sum_of_val
        self.bstToGst(root.left)
        return root