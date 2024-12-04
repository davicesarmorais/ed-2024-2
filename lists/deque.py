class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    