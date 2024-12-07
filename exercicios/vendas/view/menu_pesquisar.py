from .menu_base import MenuBase
from services import *
from models import *


class MenuPesquisar(MenuBase):
    def __init__(self, contexto: Contexto) -> None:
        opcoes = {
            "1": (self.cliente, "Cliente"),
            "2": (self.produto, "Produto"),
            "3": (self.pedido, "Pedido"),
            "4": (self.fechar_menu, "Sair")
        }
        
        super().__init__("Pesquisar", opcoes, contexto)
        
        
    def cliente(self) -> None:
        pass
    
    def produto(self) -> None:
        pass
    
    def pedido(self) -> None:
        pass
