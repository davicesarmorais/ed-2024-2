from typing import Any

class StackError(Exception):
    pass

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.__size = 0
        
    def __str__(self) -> str:
        s = ''
        for data in self:
            if s == '':
                s += f'{data} <- TOP\n'
            else:
                s += f"{data}\n"
        return s
    
    def __iter__(self) -> Any:
        current = self.top
        while current:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        return self.__size
        
    def push(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.__size += 1
        
    def peek(self) -> Any:
        if self.is_empty():
            raise StackError("Stack is empty")
        
        return self.top.data
    
    def pop(self) -> Any:
        if self.is_empty():
            raise StackError("Stack is empty")
        
        removed = self.top.data
        self.top = self.top.next
        self.__size -= 1
        return removed
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def invert(self) -> None:
        aux = Stack()
        aux2 = Stack()
        
        while not self.is_empty():
            aux.push(self.pop())
            
        while not aux.is_empty():
            aux2.push(aux.pop())
        
        while not aux2.is_empty():
            self.push(aux2.pop())
            
    def concatena(self, pilha2: 'Stack') -> None:
        pilha2.invert()
        while not pilha2.is_empty():
            self.push(pilha2.pop())
            
    def __transfere_elementos(pilha: 'Stack', pilha_final: 'Stack') -> None:
        aux1 = Stack()
        aux2 = Stack()
        while not pilha.is_empty():
            aux1.push(pilha.pop())
            aux2.push(aux1.peek())
        while not aux2.is_empty():
            pilha_final.push(aux2.pop())
            pilha.push(aux1.pop())
            
    @classmethod
    def concatena_pilhas(cls, pilha1: 'Stack', pilha2: 'Stack') -> 'Stack':
        pilha_final = Stack()
        
        cls.__transfere_elementos(pilha1, pilha_final)
        cls.__transfere_elementos(pilha2, pilha_final)
        
        return pilha_final
    
    
