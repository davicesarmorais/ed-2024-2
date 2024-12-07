class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0
    
    def __len__(self):
        return self.__size

    def __str__(self) -> str:
        s = ''
        current = self.head
        while current:
            if s != '':
                s += ' -> '

            s += str(current.data)
            current = current.next
        return s

    def show_forward(self):
        current = self.head
        while current:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=' -> ')    
            current = current.next

    def show_backward(self):
        current = self.tail
        while current:
            if current.prev is None:
                print(current.data)
            else:
                print(current.data, end=" -> ")
            current = current.prev

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
       
        self.__size += 1

    def prepend(self, data):
        if self.head is None and self.tail is None:
            return self.append()
        
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.__size += 1


    def insert(self, data, position):
        pass  # Insere na posição

    def remove(self, data):
        if len(self) == 1:
            self.pop()

        node = self.find(data)
        if node is None:
            return None
        
        # TODO

    def pop(self):
        if len(self) == 0:
            return None
        
        if len(self) == 1:
            removed = self.head.data
            self.head = None
            self.tail = None
            self.__size -= 1
            return removed
    
        removed = self.tail.data
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.__size -= 1
        return removed

            
    def pop_left(self):
        if len(self) == 0:
            return None
        
        if len(self) == 1:
            self.pop()

        removed = self.head.data
        self.head.next.prev = None
        self.head = self.head.next
        self.__size -= 1
        return removed
        

    def find(self, data):
        from_left = self._find_from_left(self.head, data)
        from_right = self._find_from_right(self.tail, data)
        
        if from_left is not None:
            return from_left
        if from_right is not None:
            return from_right

        return None
    
        
    def _find_from_left(self, node, data):
        if node is None:
            return None
        
        if node.data == data:
            return node

        return self._find_from_left(node.next, data)

    def _find_from_right(self, node, data):
        if node is None:
            return None
        
        if node.data == data:
            return node

        return self._find_from_right(node.prev, data)

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    dbll = DoublyLinkedList()

    dbll.append(2)
    dbll.append(3)
    dbll.prepend(1)
    dbll.append(4)
    dbll.append(5)
    dbll.show_forward()



    # dbll.pop()
    # dbll.show_forward()
    # dbll.pop_left()
    # dbll.show_forward()
    # dbll.show_backward()
    # dbll.pop()
    # dbll.show_forward()
    # dbll.show_backward()
    # dbll.pop()
    # dbll.show_forward()
    # dbll.show_backward()
    # dbll.pop()
    # dbll.show_forward()
    # dbll.show_backward()