import pprint
import json
from objetos import Usuario, Produto, Pedido


class Data:
    def __init__(self):
        self.data = self.__open_file()

    def __str__(self):
        return pprint.pformat(self.data)

    def __open_file(self) -> dict:
        try:
            with open("data.json", "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}

    def __save_file(self, data: dict) -> None:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def buscar_usuario(self, cpf: str) -> dict | None:
        return next((u for u in self.data["usuarios"] if u["cpf"] == cpf), None)

    def buscar_produto(self, id_produto: int) -> dict:
        return next((p for p in self.data["produtos"] if p["id"] == id_produto), None)

    def buscar_pedido(self, id_pedido: int) -> dict:
        return next((p for p in self.data["pedidos"] if p["id"] == id_pedido), None)

    def buscar_produto_por_nome(self, nome: str) -> list | None:
        return [
            produto
            for produto in self.data["produtos"]
            if nome.lower() in produto["nome"].lower()
        ]

    def cadastrar(self, objeto) -> None:
        if isinstance(objeto, Usuario):
            if self.buscar_usuario(objeto.cpf):
                raise ValueError(f"Usuário com CPF {objeto.cpf} já está cadastrado.")
            self.data["usuarios"].append(vars(objeto))

        elif isinstance(objeto, Produto):
            objeto.id = len(self.data["produtos"]) + 1
            self.data["produtos"].append(vars(objeto))

        elif isinstance(objeto, Pedido):
            objeto.id = len(self.data["pedidos"]) + 1
            self.data["pedidos"].append(vars(objeto))

        else:
            raise ValueError("Tipo de objeto não suportado para cadastro.")

        self.__save_file(self.data)

    def listar_usuarios(self) -> None:
        for usuario in self.data["usuarios"]:

            print(f"CPF: {usuario['cpf']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
            print(f"Senha: {''.join('*' for _ in usuario['senha'])}")
            print("-" * 20)

    def listar_produtos(self) -> None:
        for produto in self.data["produtos"]:
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Descricão: {produto['descricao']}")
            print(f"Preço: {produto['preco']}")
            print("-" * 20)

    def listar_pedidos(self) -> None:
        for pedido in self.data["pedidos"]:
            print(f"ID do pedido: {pedido['id']}")
            usuario_encontrado = self.buscar_usuario(pedido["cpf"])
            if usuario_encontrado:
                print(f"Usuario: {usuario_encontrado['nome']}")

            print("Produtos selecionados:")
            for id_produto in pedido["produtos"]:
                print(f"\tID do produto: {id_produto}")
                produto = self.buscar_produto(id_produto)
                print(f"\tNome: {produto['nome']}")
                print(f"\tDescricão: {produto['descricao']}")
                print(f"\tPreço: {produto['preco']}")
                print(f"\tData: {pedido['data']}")
                print("\t" + ("-" * 20))

            print(f"Total do pedido: R${pedido['total_pedido']:.2f}")
            print("\n")
