from models.pedido import Pedido
from utils.utils import *

class PedidoService:
    def __init__(self):
        self.__pedidos: dict = carregar('data/pedidos.bin')
        
    def __str__(self):
        return str(self.__pedidos)
    
    def listar(self) -> None:
        for pedido in self.__pedidos.values():
            print(pedido)
        
    def cadastrar(self, pedido: Pedido):
        self.__pedidos[pedido.id] = pedido
        salvar('data/pedidos.bin', self.__produtos)
        
    def buscar(self, pedido: int):
        return self.__pedidos.get(pedido)
    
    def remover(self, pedido: int):
        self.__pedidos.pop(pedido)
        
    
