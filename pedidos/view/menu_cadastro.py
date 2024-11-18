from .menu_base import MenuBase
from models import *
from services import *


class MenuCadastro(MenuBase):
    def __init__(self, produtos: ProdutoService, pedidos: PedidoService, clientes: ClienteService) -> None:
        super().__init__("Cadastro", {
            "1": (self.cliente, "Cliente"),
            "2": (self.produto, "Produto"),
            "3": (self.pedido, "Pedido"),
            "4": (self.fechar_menu, "Sair")
        })
        self.produtos = produtos
        self.pedidos = pedidos
        self.clientes = clientes
        
        
    def cliente(self) -> None:
        pass
    
    def produto(self) -> None:
        pass
    
    def pedido(self) -> None:
        pass
