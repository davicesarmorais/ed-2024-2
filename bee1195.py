class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def prefixo(self):
        pass
    
    def infixo(self):
        pass
    
    def posfixo(self):
        pass
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        current = self.root
        while current:
            if data > current.data:
                if current.right is None:
                    break
                current = current.right
            else:
                if current.left is None:
                    break
                current = current.left
        
        new_node = Node(data)
        if data > current.data:
            current.right = new_node
        else:
            current.left = new_node
        
    def __preorder(self, node):
        if( node != None):
            print(f'{node.data} ',end='')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __inorder(self, node):
        if( node != None):
            self.__inorder(node.left)
            print(f'{node.data} ',end='')
            self.__inorder(node.right)

    def __postorder(self, node):
        if( node != None):
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(f'{node.data} ',end='')

tree = BinaryTree()
a = [8, 3, 10, 14, 6, 4, 13, 7, 1]
for i in a:
    tree.add(i)

tree.print_right()