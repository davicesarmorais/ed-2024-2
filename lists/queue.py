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
        if self.is_empty():
            return "Empty"
        
        s = ""
        current = self.head
        while current:
            s += f"{' -> ' if s != '' else ''}{current.data}"
            current = current.next
        return s
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        
        removed = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed
    
    def peek(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self.head.data
    
fila = Queue()

fila.enqueue(1)
print(fila)
fila.enqueue(2)
print(fila)
fila.enqueue(3)
print(fila)

fila.dequeue()
print(fila)
fila.dequeue()
print(fila)
fila.dequeue()
print(fila)
