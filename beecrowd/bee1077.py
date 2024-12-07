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

def prioridade(operacao: str):
    prioridade = {
        "(": 1,
        ")": 1,
        "-": 2,
        "+": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return prioridade.get(operacao)


def eh_operando(char: str):
    if prioridade(char) is None:
        return True
    return False

def eh_operador(char: str):
    if eh_operando(char):
        return False
    return True

def in_to_pos(operacao: str):
    pos = ""
    pilha = Stack()
    for char in operacao:
        if eh_operando(char):
            pos += char
        elif char == "(":
            pilha.push(char)
        elif char == ")":
            while pilha.peek() != "(":
                pos += pilha.pop()
            pilha.pop()
        else:
            while (not pilha.is_empty()) and prioridade(char) <= prioridade(pilha.peek()):
                pos += pilha.pop()
            pilha.push(char)

    while not pilha.is_empty():
        pos += pilha.pop()
    
    return pos


n = int(input())
for _ in range(n):
    expressao = input().strip()
    print(in_to_pos(expressao))

    