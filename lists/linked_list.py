class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0
        
    def __str__(self) -> str:
        s = ''
        current = self.head
        while current:
            if s != '':
                s += ' -> '
            
            s += str(current.data)
            current = current.next
        return s
    
    def __len__(self) -> int:
        return self.__size
    
    def append(self, data):
        self.insert(data, len(self))

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.__size += 1
    
    def insert(self, data, position: int):
        position = self.__resolve_index(position)
        
        if position == 0:
            return self.prepend(data)
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
            
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.__size += 1
    
    def remove(self, data):
        if self.is_empty():
            return None
        
        if self.head.data == data:
            return self.pop_left()
        
        current = self.head
        while current.next.next and current.next.data != data:
            current = current.next
            
        current.next = current.next.next
        self.__size -= 1
        return data
        
    def pop(self):
        if len(self) == 1:
            return self.pop_left()
        
        if self.is_empty():
            return None
        
        current = self.head
        while current.next.next:
            current = current.next
        removed = current.next.data
        current.next = None
        self.__size -= 1
        return removed
    

    def pop_left(self):
        if self.is_empty():
           return None 
        
        removed = self.head.data
        self.head = self.head.next
        self.__size -= 1
        return removed


    def find(self, data):
        if self.is_empty():
            return None
        
        current = self.head
        while current.next and current.data != data:
            current = current.next
        
        if current.data == data:
            return current

    def is_empty(self):
        return len(self) == 0
    
    def __resolve_index(self, index: int):
        if index < 0:
            index += len(self)
            
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        
        return index


comandos = [
    ["prepend", 3],
    ["prepend", 2],
    ["prepend", 1],
    ["append", 4],
    ["append", 5],
    ["pop"],
    ["prepend", 2],
    ["insert", 6, 4],
    ["pop_left"],
    ["insert", 0, 0],
]


ll = LinkedList()
for idx, i in enumerate(comandos ,start=1):
    print(f"{idx}. {i[0]}({', '.join(str(x) for x in i[1:])}) ".ljust(40, '-'))
    print("\t{ Lista antes } { len:", len(ll), "}")
    if len(ll) > 0:
        print('\t', ll, sep='')
    else:
        print('\tLista vazia')
    
    print("\n\tRetorno do metodo: ", end='')
    print(getattr(ll, i[0])(*i[1:]))
    
    print("\n\t{ Lista Depois } { len:", len(ll), "}")
    if len(ll) > 0:
        print('\t', ll, sep='')
    else:
        print('\tLista vazia')
    print('\n')
    
