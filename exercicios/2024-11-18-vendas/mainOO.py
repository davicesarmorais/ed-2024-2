from gerenciador_pedidos import GerenciadorPedidos
from gerenciador_produtos import GerenciadorProdutos
from menu import *


def main():
    produtos = GerenciadorProdutos()
    pedidos = GerenciadorPedidos()
    while True:
        menu_principal = [
            "1. Cadastrar Produtos",
            "2. Listar Produtos",
            "3. Pesquisar Produtos",
            "4. Fazer Pedido",
            "5. Listar Pedidos",
            "6. Pesquisar Pedido",
            "7. Sair"
        ]
        
        limpar_tela()
        imprimir_menu(menu_principal)
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            cadastrar_produto(produtos)
        
        elif opcao == 2:
            limpar_tela()
            print(produtos)
            input("\nAperte enter para continuar...")
            
        elif opcao == 3:
            pesquisar_produto(produtos)
            
        elif opcao == 4:
            fazer_pedido(pedidos, produtos)
            
        elif opcao == 5:
            limpar_tela()
            print(pedidos)
            input("\nAperte enter para continuar...")
            
        elif opcao == 6:
            pesquisar_pedido(pedidos)
            
        elif opcao == 7:
            break
        
        
if __name__ == "__main__":
    main()