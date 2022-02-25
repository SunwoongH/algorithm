class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
class BinarySearchTree:
    def __init__(self):
        self.__root = None
        
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
        def _insert(node: TreeNode, key) -> None:
            if not node:
                return TreeNode(key)
            if key == node.key:
                return node
            elif key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.__root = _insert(self.__root, key)
    
    def delete(self, key) -> None:
        def _delete_by_copy(node: TreeNode, key) -> None:
            if not node:
                return node
            if key < node.key:
                node.left = _delete_by_copy(node.left, key)
            elif key > node.key:
                node.right = _delete_by_copy(node.right, key)
            else:
                if node.left and node.right:
                    target = node.right
                    while target.left:
                        target = target.left
                    node.key = target.key
                    node.right = _delete_by_copy(node.right, target.key)
                else:
                    return node.left or node.right
            return node
        self.__root = _delete_by_copy(self.__root, key)
        
    def traversal(self) -> None:
        def _inorder(node: TreeNode) -> None:
            if not node:
                return
            _inorder(node.left)
            print(node.key, end=' ')
            _inorder(node.right)
        _inorder(self.__root)
        print()