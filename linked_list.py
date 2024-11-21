class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.__len = 0
        
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
        return self.__len

    
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.__len += 1
    
    def append(self, data):
        self.insertAt(len(self), data)

    def insertAt(self, index, data):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        if index < 0:
            index += len(self) + 1

        if index > len(self):
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.__len += 1
    
    
    def removeAtBegin(self):
        if len(self) > 0:
            removed = self.head.data
            self.head = self.head.next
            self.__len -= 1
            return removed
    
    
    def removeAt(self, index):
        if index < 0:
            index += len(self) + 1
        
        if index > len(self):
            raise IndexError("Index out of range")
        
        if index == 0:
            return self.removeAtBegin()
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        removed = current.next.data
        current.next = current.next.next
        self.__len -= 1
        return removed


    def pop(self):
        return self.removeAt(len(self) - 1)




comandos = [
    ["insertAtBegin", 3],
    ["insertAtBegin", 2],
    ["insertAtBegin", 1],
    ["append", 4],
    ["append", 5],
    ["pop"],
    ["insertAtBegin", 2],
    ["insertAt", 4, 6],
    ["removeAtBegin"],
    ["removeAt", 4],
    ["removeAt", 0],
    ["insertAt", 0, 0],
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
    
