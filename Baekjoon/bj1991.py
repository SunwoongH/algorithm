'''
Created by sunwoong on 2022/03/06
'''
import sys
import collections

class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.__root = None
    
    def search(self, key):
        def _bfs(node: TreeNode, key):
            queue = collections.deque([node])
            while queue:
                node = queue.popleft()
                if node:
                    if node.key == key:
                        return node
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return _bfs(self.__root, key)
        
    def insert(self, key, left, right) -> None:
        if not self.__root:
            self.__root = TreeNode(key)
            if left:
                self.__root.left = TreeNode(left)
            if right:
                self.__root.right = TreeNode(right)
            return
        node = self.search(key)
        if node:
            if left:
                node.left = TreeNode(left)
            if right:
                node.right = TreeNode(right)
    
    def preorder(self) -> None:
        def _preorder(node: TreeNode) -> None:
            if not node:
                return
            print(node.key, end='')
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.__root)
        print()
        
    def inorder(self) -> None:
        def _inorder(node: TreeNode) -> None:
            if not node:
                return
            _inorder(node.left)
            print(node.key, end='')
            _inorder(node.right)
        _inorder(self.__root)
        print()
    
    def postorder(self) -> None:   
        def _postorder(node: TreeNode) -> None:
            if not node:
                return
            _postorder(node.left)
            _postorder(node.right)
            print(node.key, end='')
        _postorder(self.__root)
        print()
    
n = int(sys.stdin.readline())
tree = BinaryTree()
for _ in range(n):
    key, left, right = map(str, sys.stdin.readline().rstrip('\n').split())
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree.insert(key, left, right)
tree.preorder()
tree.inorder()
tree.postorder()