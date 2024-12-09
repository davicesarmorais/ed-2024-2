from gerenciador import GerenciadorPilhas
from pilha import Stack
import platform, os, subprocess

def clear() -> None:
    """Limpa a tela do terminal."""
    if platform.system() == "Windows" and os.getenv("TERM") != "xterm":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def main():
    gerenciador = GerenciadorPilhas()
    gerenciador.nova_pilha()
    
    while True:
        clear()
        print("Editor de Pilha")
        print("=" * 30)
        print(gerenciador)
        print("=" * 30)
        print(
            "(e) Empilhar",
            "(d) Desempilhar",
            "(t) Tamanho",
            "(o) Obter elemento do topo",
            "(v) Teste de pilha vazia",
            "(r) Criar nova Pilha",
            "(n) Inverter os elementos da pilha",
            "(z) Esvaziar a pilha",
            "(c) Concatenar duas pilhas",
            "(m) Escolher outra pilha",
            "(n) Conversão dec/bin",
            "(s) Sair",
            sep="\n",
        )
        print("=" * 30)
        opcao = input("> ").lower()
        
        if opcao == 'e':
            gerenciador.atual.push(input("Digite o elemento: "))
        elif opcao == 'd':
            gerenciador.atual.pop()
        elif opcao == 't':
            print(f"Tamanho da pilha: {len(gerenciador.atual)}")
            input("Pressione enter para continuar...")
        elif opcao == 'o':
            print(f"Elemento do topo: {gerenciador.atual.peek()}")
            input("Pressione enter para continuar...")
        elif opcao == 'v':
            print(f"Pilha vazia: {gerenciador.atual.is_empty()}")
            input("Pressione enter para continuar...")
        elif opcao == 'r':
            gerenciador.nova_pilha()
        elif opcao == 'n':
            gerenciador.atual.invert()
        elif opcao == 'z':
            gerenciador.atual.esvaziar()
        elif opcao == 'c':
            print("(1) Concatenar com a pilha atual")
            print("(2) Gerar uma nova pilha concatenando outras duas")
            opcao = input("> ")
            if opcao == '1':
                index = int(input("Digite o indice da outra pilha: "))
                if index == gerenciador.atual_indice + 1:
                    print("Nao eh possivel concatenar com a pilha atual")
                    input("\nPressione enter para continuar...")
                    continue
                
                pilha = gerenciador.buscar_pilha(index - 1)
                if pilha is None:
                    continue
                gerenciador.atual.concatena(pilha)
                # gerenciador.remove(index - 1)
                
            elif opcao == '2':
                index1 = int(input("Digite o indice da primeira pilha : "))
                pilha1 = gerenciador.buscar_pilha(index1 - 1)
                if pilha1 is None:
                    continue
                
                index2 = int(input("Digite o indice da segunda pilha: "))
                pilha2 = gerenciador.buscar_pilha(index2 - 1)
                if pilha2 is None:
                    continue
                
                gerenciador.nova_pilha(Stack.concatena_pilhas(pilha1, pilha2))
        elif opcao == 'm':
            index = int(input("Digite o indice da pilha: "))
            try:
                gerenciador.atual = index
            except IndexError:
                print("Pilha inexistente")
                input("Pressione enter para continuar...")
                
        elif opcao == 'n':
            pass
        elif opcao == 's':
            break
        
        
if __name__ == "__main__":
    main()