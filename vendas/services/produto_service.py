from models.produto import Produto
from utils.utils import *

class ProdutoService:
    def __init__(self):
        self.__produtos: dict = carregar('data/produtos.bin')
    
    def __str__(self):
        return str(self.__produtos)
        
    def listar(self) -> None:
        for produto in self.__produtos.values():
            print(produto)
    
    def cadastrar(self, produto: Produto):
        self.__produtos[produto.id] = produto
        salvar('data/produtos.bin', self.__produtos)
        
    def buscar(self, id_produto: int):
        return self.__produtos.get(id_produto)
    
    def remover(self, id_produto: int):
        self.__produtos.pop(id_produto)
        
    
