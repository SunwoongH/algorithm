'''
문제 - 이진 트리 직렬화 & 역직렬화

이진 트리를 배열로 직렬화하고 반대로 역직렬화하는 기능을 구현하라.
'''
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS(재귀) 풀이
class Codec:
    def serialize(self, root: TreeNode) -> str:
        encoding = []
        def encoding_dfs(node: TreeNode):
            if not node:
                encoding.append('#')
                return
            encoding.append(str(node.val))
            encoding_dfs(node.left)
            encoding_dfs(node.right)
        encoding_dfs(root)
        return ' '.join(encoding)
        
    def deserialize(self, data: str) -> TreeNode:
        decoding = data.split()
        self.i = -1
        def decoding_dfs() -> TreeNode:
            self.i += 1
            if decoding[self.i] != '#':
                node = TreeNode(int(decoding[self.i]))
            else:
                node = None
            if not node:
                return None
            node.left = decoding_dfs()
            node.right = decoding_dfs()
            return node
        root = decoding_dfs()
        return root

# BFS 풀이
class Codec:
    def serialize(self, root: TreeNode) -> str:
        encoding = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                encoding.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                encoding.append('#')
        return ' '.join(encoding)
        
    def deserialize(self, data: str) -> TreeNode:
        if data == '#':
            return None
        decoding = data.split()
        root = TreeNode(str(decoding[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if decoding[i] != '#':
                node.left = TreeNode(int(decoding[i]))
                queue.append(node.left)
            i += 1
            if decoding[i] != '#':
                node.right = TreeNode(int(decoding[i]))
                queue.append(node.right)
            i += 1
        return root