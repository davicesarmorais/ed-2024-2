class StackError(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.__size = 0
        
    def __str__(self):
        s = ''
        current = self.top
        while current:
            s += f"{current.data} {'<- TOP' if s == '' else ''}\n"
            current = current.next
        return s
    
    def __len__(self):
        return self.__size
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.__size += 1
        
    def peek(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        
        return self.top.data
    
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        
        removed = self.top.data
        self.top = self.top.next
        self.__size -= 1
        return removed
    
    def is_empty(self):
        return len(self) == 0
    
stack = Stack()
stack.peek()
stack.push(1)
print(stack)
stack.push(2)
print(stack)
stack.push(3)
print(stack)
