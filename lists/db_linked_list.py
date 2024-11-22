class Node:
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.__prev = None
        
    @property
    def next(self):
        return self.__next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0
    
    def __len__(self):
        return self.size

    def __str__(self):
        pass  # Representação da lista

    def append(self, data):
        pass  # Adiciona ao final

    def prepend(self, data):
        pass  # Adiciona ao início

    def insert(self, data, position):
        pass  # Insere na posição

    def remove(self, data):
        pass  # Remove o primeiro nó com o dado

    def pop(self):
        pass  # Remove o último nó

    def pop_left(self):
        pass  # Remove o primeiro nó

    def find(self, data):
        pass  # Retorna o nó com o dado

    def is_empty(self):
        return self.size == 0
