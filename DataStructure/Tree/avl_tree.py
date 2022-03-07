class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.__root = None
    
    def _get_height(self, node: TreeNode) -> int:
        return node.height if node else 0
    
    def _get_balance(self, node: TreeNode) -> int:
        return self._get_height(node.left) - self._get_height(node.right) if node else 0
    
    def _left_rotate(self, node: TreeNode) -> TreeNode:
        child = node.right
        child.left, node.right = node, child.left
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        child.height = 1 + max(self._get_height(child.left), self._get_height(child.right))
        return child
    
    def _right_rotate(self, node: TreeNode) -> TreeNode:
        child = node.left
        child.right, node.left = node, child.right
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        child.height = 1 + max(self._get_height(child.left), self._get_height(child.right))
        return child
    
    def _rebalance(self, node: TreeNode) -> TreeNode:
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        elif balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node
    
    def search(self, key) -> bool:
        def _search(node: TreeNode, key) -> bool:
            if not node:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.__root, key)
    
    def insert(self, key) -> None:
        def _insert(node: TreeNode, key):
            if not node:
                return TreeNode(key)
            if key == node.key:
                return node
            elif key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return self._rebalance(node)
        self.__root = _insert(self.__root, key)
    
    def delete(self, key) -> None:
        def _delete(node: TreeNode, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.left and node.right:
                    target = node.right
                    while target.left:
                        target = target.left
                    node.key = target.key
                    node.right = _delete(node.right, target.key)
                else:
                    return node.left or node.right
            return self._rebalance(node)
        self.__root = _delete(self.__root, key)
    
    def traversal(self) -> None:
        def _inorder(node: TreeNode) -> None:
            if not node:
                return
            _inorder(node.left)
            print(f'[key: {node.key}, height: {node.height}]', end=' ')
            _inorder(node.right)
        _inorder(self.__root)
        print()