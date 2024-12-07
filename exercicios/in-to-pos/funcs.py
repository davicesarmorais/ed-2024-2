from pilha import Stack

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