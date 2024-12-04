class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_left(self, data):
        if self.left is None:
            self.left = Node(data)
    
    def add_right(self, data):
        if self.right is None:
            self.right = Node(data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        self._add(data, self.root)
    
    
    def _add(self, data, current):
        if data < current.data:
            if current.left is not None:
                self._add(data, current.left)
            else:
                current.add_left(data)
        else:
            if current.right is not None:
                self._add(data, current.right)
            else:
                current.add_right(data)
        
    def preorder(self, node, result):
        if node is not None:
            result.append(str(node.data))
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def inorder(self, node, result):
        if node is not None:
            self.inorder(node.left, result)
            result.append(str(node.data))
            self.inorder(node.right, result)

    def postorder(self, node, result):
        if node is not None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(str(node.data))