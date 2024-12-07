import os
from produto import Produto
from pedido import Pedido, Carrinho
from gerenciador_produtos import GerenciadorProdutos
from gerenciador_pedidos import GerenciadorPedidos


def limpar_tela():
    os.system("cls ; clear")

def imprimir_menu(opcoes: list):
    for opcao in opcoes:
        print(opcao)


def exibir_produto_sendo_montado(produto: Produto):
    desc = produto.descricao
    val = produto.valor
    
    if produto.descricao is None:
        desc = 'NÃO INFORMADO'
        
    if produto.valor is None:
        val = 'NÃO INFORMADO'
    
    print("Cadastrando produto")
    print(f"Descrição: {desc}")
    print(f"Valor: {val}")
    
    
def cadastrar_produto(produtos: GerenciadorProdutos) -> None:
    produto = Produto(None, None)
    while True:
        limpar_tela()
        exibir_produto_sendo_montado(produto)

        if produto.descricao is None:
            print("\nDigite a DESCRIÇÃO do produto: ")
            descricao = input("> ")
            produto.descricao = descricao
        elif produto.valor is None:
            print("\nDigite o VALOR do produto: ")
            valor = float(input("> "))
            produto.valor = valor
        else:
            break
    
    produtos.adicionar(produto)
    print("\nProduto cadastrado!")
    input("Aperte enter para continuar...")
    
    
def pesquisar_produto(produtos: GerenciadorProdutos) -> None:
    limpar_tela()
    id_produto = int(input("Digite o Id do produto: "))
    produto = produtos.pesquisar(id_produto)
    
    if produto is None:
        print("Produto nao encontrado.")
    else:
        print(produto)
    input("Aperte enter para continuar...")
        
        
def pesquisar_pedido(pedidos: GerenciadorPedidos) -> None:
    limpar_tela()
    id_pedido = int(input("Digite o Id do pedido: "))
    pedido = pedidos.pesquisar(id_pedido)
    
    if pedido is None:
        print("Pedido nao encontrado.")
    else:
        print(pedido)
    input("Aperte enter para continuar...")
        
        
def fazer_pedido(pedidos: GerenciadorPedidos, produtos: GerenciadorProdutos) -> None:
    carrinho = Carrinho()
    while True:
        limpar_tela()
        print("-------- Produtos --------")
        print(produtos)
        print("--------------------------\n")
        
        if len(carrinho) < 1:
            print("Carrinho vazio")
        else:
            print("-------- Carrinho --------")
            print(carrinho)
            print("--------------------------")

        print("\nDigite 0 para finalizar compra.")
        print("Digite o ID do produto para adicionar ao carrinho")
        
        id_produto = int(input("> "))
        
        if id_produto == 0 and len(carrinho) == 0:
            break
        elif id_produto == 0:
            pedido = Pedido(carrinho)
            pedidos.adicionar(pedido)
            print("Compra finalizada!")
            input("Aperte enter para continuar...")
            break
        
        produto = produtos.pesquisar(id_produto)
        
        if produto is None:
            print("Produto nao encontrado.")
            input("Aperte enter para continuar...")
            continue
        
        qtd_itens = int(input("Digite a quantidade de itens: "))
        carrinho.adicionar(produto, qtd_itens)
        
    