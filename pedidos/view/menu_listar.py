from .menu_base import MenuBase
from services import *
from models import *
from utils.utils import prosseguir

class MenuListar(MenuBase):
    def __init__(self, contexto: Contexto) -> None:
        opcoes = {
            "1": (self.cliente, "Cliente"),
            "2": (self.produto, "Produto"),
            "3": (self.pedido, "Pedido"),
            "4": (self.fechar_menu, "Sair")
        }
        
        super().__init__("Listar", opcoes, contexto)
        
        
    def cliente(self) -> None:
        self.contexto.clientes.listar()
        prosseguir()

        
    def produto(self) -> None:
        self.contexto.produtos.listar()
        prosseguir()
    
    def pedido(self) -> None:
        self.contexto.pedidos.listar()
        prosseguir()

