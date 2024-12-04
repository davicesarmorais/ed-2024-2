class QueueError(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __str__(self):
        pass
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        pass
    
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
    
    def peek(self):
        pass