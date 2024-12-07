import os
import time
from data import Data


def cadastro_opcao(data: Data) -> None:
    print("---- Cadastro ----")
    print("1 - Cadastrar Usuário")
    print("2 - Cadastrar Produto")
    print("3 - Cadastrar Pedido")
    print("4 - Voltar")
    opcao = input()
    os.system("clear")

    if opcao == "1":
        cadastrar_usuario(data)
    elif opcao == "2":
        cadastrar_produto(data)
    elif opcao == "3":
        cadastrar_pedido(data)
    elif opcao == "4":
        return
    else:
        print("Opção inválida")
        return cadastro_opcao(data)

    if opcao != "4":
        input("Pressione qualquer tecla para continuar...")

    os.system("clear")


def listar_opcao(data: Data) -> None:
    print("---- Listar ----")
    print("1 - Listar Usuários")
    print("2 - Listar Produtos")
    print("3 - Listar Pedidos")
    print("4 - Voltar")
    opcao = input()
    os.system("clear")

    if opcao == "1":
        data.listar_usuarios()
    elif opcao == "2":
        data.listar_produtos()
    elif opcao == "3":
        data.listar_pedidos()
    elif opcao == "4":
        return
    else:
        print("Opção inválida")
        return listar_opcao(data)

    if opcao != "4":
        input("Pressione qualquer tecla para continuar...")

    os.system("clear")


def pesquisar_opcao(data: Data) -> None:
    print("---- Pesquisar ----")
    print("1 - Pesquisar Usuário")
    print("2 - Pesquisar Produto")
    print("3 - Pesquisar Pedido")
    print("4 - Voltar")
    opcao = input()
    os.system("clear")

    if opcao == "1":
        pesquisar_usuario(data)
    elif opcao == "2":
        pesquisar_produto(data)
    elif opcao == "3":
        pesquisar_pedido(data)
    elif opcao == "4":
        return
    else:
        print("Opção inválida")
        return pesquisar_opcao(data)

    if opcao != "4":
        input("Pressione qualquer tecla para continuar...")

    os.system("clear")


def pesquisar_usuario(data: Data) -> None:
    cpf = input("Digite o CPF ou 'q' para sair: ")
    if cpf == "q":
        return

    usuario = data.buscar_usuario(cpf)

    if not usuario:
        print("Usuário com este CPF não encontrado.")
        return pesquisar_usuario(data)

    print(f"CPF: {usuario['cpf']}")
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"Senha: {''.join('*' for _ in usuario['senha'])}")
    return


def pesquisar_produto(data: Data) -> None:
    def exibir_produto(produto):
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Descricão: {produto['descricao']}")
        print(f"Preço: {produto['preco']}")

    nome = input("Digite o nome ou o id do produto ou 'q' para sair: ")
    if nome == "q":
        return

    if nome.isdecimal():
        produto = data.buscar_produto(int(nome))
        if not produto:
            print("Nenhum produto encontrado.")
            return pesquisar_produto(data)

        exibir_produto(produto)
        return

    produtos = data.buscar_produto_por_nome(nome)
    if not produtos:
        print("Nenhum produto encontrado.")
        return pesquisar_produto(data)

    for produto in produtos:
        exibir_produto(produto)


def pesquisar_pedido(data: Data) -> None:
    id_pedido = input("Digite o ID do pedido ou 'q' para sair: ")
    if id_pedido == "q":
        return

    pedido = data.buscar_pedido(int(id_pedido))

    if not pedido:
        print("Nenhum pedido encontrado.")
        return pesquisar_pedido(data)

    print(f"ID do pedido: {pedido['id']}")
    usuario_encontrado = data.buscar_usuario(pedido["cpf"])
    if usuario_encontrado:
        print(f"Usuario: {usuario_encontrado['nome']}")

    print("Produtos selecionados:")
    for id_produto in pedido["produtos"]:
        print(f"\tID do produto: {id_produto}")
        produto = data.buscar_produto(id_produto)
        print(f"\tNome: {produto['nome']}")
        print(f"\tDescricão: {produto['descricao']}")
        print(f"\tPreço: {produto['preco']}")
        print(f"\tData: {pedido['data']}")
        print("\t" + ("-" * 20))

    print(f"Total do pedido: R${pedido['total_pedido']:.2f}")
    print("\n")


def cadastrar_usuario(data: Data) -> None:
    atributos = {"cpf": None, "nome": None, "email": None, "senha": None}

    for atributo in atributos:
        entrada = input(f"Digite o {atributo} ou 'q' para sair: ")

        if atributo == "cpf" and data.buscar_usuario(entrada):
            print("Usuário com este CPF é cadastrado.")
            return cadastrar_usuario()

        if entrada == "q":
            return

        atributos[atributo] = entrada

    usuario = Usuario(**atributos) # type: ignore
    data.cadastrar(usuario)
    print("Usuário cadastrado com sucesso.")
    return


def cadastrar_produto(data: Data) -> None:
    atributos = {"nome": None, "descricao": None, "preco": None}
    for atributo in atributos:
        entrada = input(f"Digite o {atributo} ou 'q' para sair: ")

        if atributo == "nome" and data.nome_produto_cadastrado(entrada):
            print("Produto com este nome já cadastrado.")
            print("Tem certeza que quer continuar?")
            if input("Digite 's' para sim ou 'n' para cancelar: ") != "s":
                return cadastrar_produto()

        if entrada == "q":
            return

        atributos[atributo] = entrada

    produto = Produto(**atributos) # type: ignore
    data.cadastrar(produto)
    print("Produto cadastrado com sucesso.")
    return


def cadastrar_pedido(data: Data) -> None:
    cpf = input("Digite o CPF ou 'q' para cancelar: ")
    if cpf == "q":
        return

    if not data.buscar_usuario(cpf):
        print("Usuário com este CPF não está cadastrado.")
        time.sleep(1)
        return cadastrar_pedido()

    total_pedido = 0
    produtos_ids = []
    produtos_selecionados = []
    while True:
        os.system("clear")
        data.listar_produtos()

        if not produtos_selecionados:
            print("Pedido vazio")
        else:
            print(f"Pedido: {produtos_selecionados}")

        print("Digite 'q' para voltar ou '0' para terminar a compra:")
        id_produto = input("> ")

        if id_produto in "q":
            break

        if (id_produto == "0") and not produtos_ids:
            print("Nenhum produto adicionado ao pedido.")
            time.sleep(1)
            continue

        if (id_produto == "0") and produtos_ids:
            pedido = Pedido(cpf, produtos_ids, total_pedido) # type: ignore
            data.cadastrar(pedido)
            print("Pedido criado com sucesso.")
            return

        if not id_produto.isdecimal() or not (
            produto := data.produto_por_id(int(id_produto))
        ):
            print("Produto não encontrado.")
            time.sleep(1)
            continue

        if int(id_produto) in produtos_ids:
            print("Produto ja adicionado.")
            time.sleep(1)
            continue

        produtos_ids.append(int(id_produto))
        produtos_selecionados.append(produto["nome"])
        total_pedido += produto["preco"]
        print(f"Produto {produto['nome']} adicionado ao pedido.")
        time.sleep(1)
