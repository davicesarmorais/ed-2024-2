from .produto import Produto
import datetime

class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos = {}

    def __str__(self) -> str:
        return f'\n{"-" * 20}\n'.join([
            f"{produto.__str__()}\nQuantidade: {quantidade}" for produto, quantidade in self.__produtos.items()
            ])

    def adicionar_produto(self, produto: Produto, quantidade: int) -> None:
        self.__produtos[produto] = quantidade
        
    def remover_produto(self, produto: Produto) -> None:
        if produto in self.__produtos:
            self.__produtos.pop(produto)
    

class Pedido:
    __serial = 0

    def __init__(self, cpf_cliente: str = None, produtos: CarrinhoCompras = None) -> None:
        self.__cpf = cpf_cliente
        self.__produtos = produtos
        self.__data = datetime.datetime.now().strftime("%d-%m-%Y")
        self.__total_pedido = sum(p.preco * qtd for p, qtd in produtos.items())
        self.__id = Pedido.__serial + 1

    def __str__(self) -> str:
        return '\n'.join([
            f"ID PEDIDO: {self.id}",
            f"CPF do cliente: {self.cpf_cliente}", 
            f"Total: R$ {self.total_pedido:.2f}", 
            f"Data: {self.data}",
            f"Produtos Selecionados: \n{self.produtos}", 
        ])
        
    def __eq__(self, other) -> bool:
        if isinstance(other, Pedido):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id) 

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def cpf_cliente(self) -> str:
        return self.__cpf
    
    @property
    def produtos(self) -> str:
        return self.__produtos
    
    @property
    def total_pedido(self) -> float:
        return round(self.__total_pedido, 2)
    
    @property
    def data(self) -> str:
        return self.__data
    
    # @id.setter
    # def id(self, id: int):
    #     if not self.validar_id(id):
    #         raise ValueError("ID inválido")

    #     self.id = id

    @staticmethod
    def validar_id(id_produto: int) -> bool:
        return isinstance(id_produto, int)

if __name__ == "__main__":
    produtos_selecionados = {
        Produto(1, "1", 1.0): 1,
        Produto(2, "2", 2.2): 2
    }

    pedido = Pedido(1, "12345678910", produtos_selecionados)