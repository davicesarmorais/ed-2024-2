from models.cliente import Cliente
from utils.utils import *

class ClienteService:
    def __init__(self):
        self.__clientes: dict = carregar('data/clientes.bin')
    
    def __str__(self):
        return str(self.__clientes)
    
    def listar(self) -> None:
        for cliente in self.__clientes.values():
            print(cliente)
    
    def cadastrar(self, cliente: Cliente):
        self.__clientes[cliente.cpf] = cliente
        salvar('data/clientes.bin', self.__produtos)
        
    def buscar(self, id_cliente: int):
        return self.__clientes.get(id_cliente)
    
    def remover(self, id_cliente: int):
        self.__clientes.pop(id_cliente)
        
    