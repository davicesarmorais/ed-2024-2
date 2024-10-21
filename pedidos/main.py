import os
from data import Data
from funcs import *


def main():
    data = Data()
    while True:
        print("---- Menu Principal ----")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Pesquisar")
        print("4 - Sair")
        opcao = input()
        os.system("clear")

        match opcao:
            case "1":
                cadastro_opcao(data)

            case "2":
                listar_opcao(data)

            case "3":
                pesquisar_opcao(data)

            case "4":
                break

            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
