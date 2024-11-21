from models.pedido import Pedido
from utils.utils import *

class PedidoService:
    def __init__(self):
        self.__pedidos: dict = carregar('data/pedidos.bin')
        self.__current_id = self.get_id()
        
    def __str__(self):
        return str(self.__pedidos)
            
    def get_id(self):
        current_id = self.__pedidos.get("current_id")
        if not current_id:
            current_id = self.__pedidos["current_id"] = max(self.__pedidos)
        return current_id

    def listar(self) -> None:
        for pedido in self.__pedidos.values():
            print(pedido)
        
    def cadastrar(self, pedido: Pedido):
        pedido.id = self.__current_id
        self.__pedidos[pedido.id] = pedido
        salvar('data/pedidos.bin', self.__produtos)
        
    def buscar(self, pedido: int):
        return self.__pedidos.get(pedido)
    
    def remover(self, pedido: int):
        self.__pedidos.pop(pedido)
        
    
