class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.__size = 0

    def __len__(self):
        return self.__size
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.__size += 1
        
    def peek(self):   
        return self.top.data
    
    def pop(self):
        removed = self.top.data
        self.top = self.top.next
        self.__size -= 1
        return removed
    
    def is_empty(self):
        return len(self) == 0