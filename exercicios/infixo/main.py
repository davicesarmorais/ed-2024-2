from utils import operacao_valida, clear
from menu import *


def main():
    while True:
        while True:
            print("Digite a expressão ou '.' para sair: ")
            expressao = input("> ")
            if expressao == ".":
                return
            
            try:
                operacao_valida(expressao)
                break
            except Exception as e:
                clear()
                print(e)
                continue

        while True:
            clear()
            print("----- EXPRESSÃO -----")
            print(expressao)
            print("---------------------")
            print(
                "(c) converter expressao",
                "(a) avaliar resultado da expressao",
                "(d) digitar outra expressao",
                "(s) sair",
                sep="\n"
            )
            opcao = input("> ").lower()

            if opcao == "c":
                converter(expressao)
                    
            elif opcao == "a":
                pos = in_to_pos(expressao)
                avaliar(pos)
                    
                
            elif opcao == "d":
                clear()
                break
            
            elif opcao == "s":
                return
            
    
if __name__ == "__main__":
    main()