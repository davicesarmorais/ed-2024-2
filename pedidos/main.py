import os,time
from data import Data
from objetos import Usuario, Produto, Pedido

def cadastrar_usuario():
    atributos = {'cpf': None, 'nome':None, 'email':None, 'senha': None}
    
    for atributo in atributos:
        entrada = input(f"Digite o {atributo} ou 'q' para sair: ")
        if atributo == 'cpf' and data.usuario_cadastrado(entrada):
            print("Usuário com este CPF é cadastrado.")
            return cadastrar_usuario()
        
        if atributo == 'q':
            return

        atributos[atributo] = entrada
        
    usuario = Usuario(**atributos)
    data.cadastrar(usuario)
    print("Usuário cadastrado com sucesso.")
    return

def cadastrar_produto():
    atributos = {'nome': None, 'descricao':None, 'preco':None}
    for atributo in atributos:
        entrada = input(f"Digite o {atributo} ou 'q' para sair: ")
        
        if atributo == 'nome' and data.nome_produto_cadastrado(entrada):
            print("Produto com este nome já cadastrado.")
            print("Tem certeza que quer continuar?")
            if input("Digite 's' para sim ou 'n' para cancelar: ") != 's':
                return cadastrar_produto()
        
        if entrada == 'q':
            return
        
        atributos[atributo] = entrada
    

    produto = Produto(**atributos)
    data.cadastrar(produto)
    print("Produto cadastrado com sucesso.")
    return

def cadastrar_pedido():
    cpf = input("Digite o CPF ou 'q' para cancelar: ")
    if cpf == 'q':
        return
    
    if not data.usuario_cadastrado(cpf):
        print("Usuário com este CPF não está cadastrado.")
        time.sleep(1)
        return cadastrar_pedido()
    
    total_pedido = 0
    produtos_ids = []
    produtos_selecionados = []
    while True:
        os.system('clear')
        data.listar_produtos()
        
        if not produtos_selecionados:
            print("Pedido vazio")
        else:
            print(f"Pedido: {produtos_selecionados}")
        
        print("Digite 'q' para voltar ou '0' para terminar a compra:")
        id_produto = input("> ")
        
        if id_produto in 'q':
            break
        
        if (id_produto == '0') and not produtos_ids:
            print("Nenhum produto adicionado ao pedido.")
            time.sleep(1)
            continue
        
        if (id_produto == '0') and produtos_ids:
            pedido = Pedido(cpf, produtos_ids, total_pedido)
            data.cadastrar(pedido)
            print("Pedido criado com sucesso.")
            return
        
        
        if not id_produto.isdecimal() or not (produto := data.produto_por_id(int(id_produto))):
            print("Produto não encontrado.")
            time.sleep(1)
            continue
        
        if int(id_produto) in produtos_ids:
            print("Produto ja adicionado.")
            time.sleep(1)
            continue
        
        produtos_ids.append(int(id_produto))
        produtos_selecionados.append(produto['nome'])
        total_pedido += produto['preco']
        print(f"Produto {produto['nome']} adicionado ao pedido.")
        time.sleep(1)


data = Data()
while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar Usuário")
    print("2 - Cadastrar Produto")
    print("3 - Cadastrar Pedido")
    print("4 - Listar Usuários")
    print("5 - Listar Produtos")
    print("6 - Listar Pedidos")
    print("7 - Sair")
    opcao = input()
    os.system('clear')
    
    match opcao:
        case "1":
            cadastrar_usuario()
        case "2":
            cadastrar_produto()
        case "3":
            cadastrar_pedido()
        case "4":
            data.listar_usuarios()
        case "5":
            data.listar_produtos()
        case "6":
            data.listar_pedidos()
        case "7":
            break
        case _:
            print("Opção inválida. Tente novamente.")
        
    input("Pressione qualquer tecla para continuar...")
    os.system('clear')