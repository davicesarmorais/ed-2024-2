from typing import Optional
from pilha import Stack
from tabulate import tabulate
import os
import platform
import subprocess


def clear() -> None:
    """Limpa a tela do terminal."""
    if platform.system() == "Windows" and os.getenv("TERM") != "xterm":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


def prioridade(char: str) -> Optional[int]:
    prioridade = {
        "(": 1,
        ")": 1,
        "-": 2,
        "+": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return prioridade.get(char)

def eh_operando(char: str) -> bool:
    return prioridade(char) is None

def eh_operador(char: str) -> bool:
    return not eh_operando(char)

def in_to_pos(expressao: str, visual: bool = False) -> str:
    cabecalho = ["Passo", "CHAR", "Pilha", "Saida"]
    dados = []
    passo = 1
    
    expressao = expressao.replace(" ", "")
    pos = ""
    pilha = Stack()

    for char in expressao:
        if eh_operando(char):
            pos += char
        elif char == "(":
            pilha.push(char)
        elif char == ")":
            while pilha.peek() != "(":
                pos += pilha.pop()
            pilha.pop()
        else:
            while (not pilha.is_empty()) and (prioridade(char) <= prioridade(pilha.peek())):
                pos += pilha.pop()
            pilha.push(char)

        dados.append([passo, char, str(pilha), pos])
        passo += 1
        
    while not pilha.is_empty():
        pos += pilha.pop()
        dados.append([passo, char, str(pilha), pos])
        passo += 1
    
    if visual:
        print(tabulate(dados, headers=cabecalho))

    return pos


def in_to_pre(expressao: str) -> str:
    expressao = expressao.replace(" ", "")
    expressao_tratada = ""
    for char in expressao[::-1]:
        if char == "(":
            expressao_tratada += ")"
        elif char == ")":
            expressao_tratada += "("
        else:
            expressao_tratada += char
    pos = in_to_pos(expressao_tratada)
    return pos[::-1]
    
def resultado(expressao: str, variaveis: dict) -> bool:
    pilha = Stack()
    operadores = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: a ** b
    }
    for char in expressao:
        if eh_operando(char):
            pilha.push(variaveis[char])
        elif eh_operador(char):
            b = pilha.pop()
            a = pilha.pop()
            pilha.push(operadores[char](a, b))
    return pilha.peek()


def parenteses_balancados(expressao: str) -> bool:
    expressao = expressao.replace(" ", "")
    pilha = []
    for char in expressao:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if len(pilha) == 0:
                return False
            pilha.pop()
    
    return len(pilha) == 0
    
def sequencia_operadores_operandos_valida(expressao: str) -> bool:
    operadores = {'+', '-', '*', '/', '^'}
    anterior = None

    for i, char in enumerate(expressao):
        if char in operadores:
            # Se houver dois operadores seguidos OU se o operador estiver no começo ou no final
            if anterior in operadores or anterior is None or i == len(expressao) - 1:
                return False

        elif char == '(':
            # Parêntese de abertura pode estar no início, após um operador ou outro parêntese de abertura
            if anterior is not None and anterior not in operadores and anterior != '(':
                return False

        elif char == ')':
            # Parêntese de fechamento não pode estar após um operador ou após outro parêntese de abertura
            if anterior in operadores or anterior == '(' or anterior is None:
                return False
        
        anterior = char

    return True


def contem_apenas_caracteres_validos(expressao: str) -> bool:
    for char in expressao:
        if not (char.isalnum() or char in "^+-*/()"):
            return False
    return True


def operacao_valida(expressao: str) -> None:
    expressao = expressao.replace(" ", "")
    if not contem_apenas_caracteres_validos(expressao):
        raise Exception("Caracteres invalidos")
    
    if not parenteses_balancados(expressao):
        raise Exception("Parenteses nao balanceados")
    
    if not sequencia_operadores_operandos_valida(expressao):
        raise Exception("Sequencia de operadores e operandos invalida")


