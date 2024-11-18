from .produto import Produto
from models.cliente import Cliente
import datetime

class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos = {}

    def __str__(self) -> str:
        return f'\n{'-' * 20}\n'.join([
            f"{produto.__str__()}\nQuantidade: {quantidade}" for produto, quantidade in self.__produtos.items()
            ])

    def adicionar_produto(self, produto: Produto, quantidade: int) -> None:
        self.__produtos[produto] = quantidade
        
    def remover_produto(self, produto: Produto) -> None:
        if produto in self.__produtos:
            self.__produtos.pop(produto)
    

class Pedido:
    def __init__(self, id_pedido: int, cpf_cliente: str, produtos: CarrinhoCompras) -> None:
        self.__id = id_pedido
        self.__cpf = cpf_cliente
        self.__produtos = produtos
        self.__data = datetime.datetime.now().strftime("%d-%m-%Y")
        self.__total_pedido = sum(p.preco * qtd for p, qtd in produtos.items())

    def __str__(self) -> str:
        return '\n'.join([
            f"ID PEDIDO: {self.id_pedido}",
            f"Nome do cliente: {self.cpf_cliente}", 
            f"Total: R$ {self.total_pedido:.2f}", 
            f"Data: {self.data}",
            f"Produtos Selecionados: \n{self.produtos}", 
        ])
        
    def __eq__(self, other) -> bool:
        if isinstance(other, Pedido):
            return self.id_pedido == other.id_pedido
        return False

    def __hash__(self) -> int:
        return hash(self.id_pedido) 

    @property
    def id_pedido(self) -> int:
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
    
    
if __name__ == "__main__":
    produtos_selecionados = {
        Produto(1, "1", 1.0): 1,
        Produto(2, "2", 2.2): 2
    }

    pedido = Pedido(1, "12345678910", produtos_selecionados)