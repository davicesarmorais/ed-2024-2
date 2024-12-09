from typing import Optional
from utils import in_to_pos, in_to_pre, clear, eh_operando, resultado

def converter(expressao: str) -> None:
    while True:
        print(
            "(1) infixo para posfixo",
            "(2) infixo para prefixo",
            "(3) ambos",
            "(4) cancelar",
            sep="\n"
        )
        opcao = input("> ").lower()
        if opcao == "4":
            return None

        if opcao == "1":
            print("(1) apenas o resultado\n(2) passo a passo")
            opcao = input("> ")
            if opcao in "1":    
                print(f"\nPos: {in_to_pos(expressao)}")
                
            elif opcao == "2":
                clear()
                print(f"\nPos: {in_to_pos(expressao, visual=True)}")
            
        elif opcao == "2":
            print(f"\nPre: {in_to_pre(expressao)}")
        elif opcao == "3":
            print(f"\nPos: {in_to_pos(expressao)}\nPre: {in_to_pre(expressao)}")
            
        input("\nPressione enter para continuar...")
        return

def avaliar(expressao: str) -> Optional[str]:
    print(
        "Digite os valores das variáveis ou '.' para cancelar:",
    )
    variaveis = {}
    for char in expressao:
        if eh_operando(char):
            variaveis[char] = None

    for char in variaveis:
        entrada = input(f"{char}: ")
        if entrada == '.':
            return None
        
        variaveis[char] = float(entrada)
        
    print(f"\nResultado: {resultado(expressao, variaveis)}")
    input("\nPressione enter para continuar...")
    