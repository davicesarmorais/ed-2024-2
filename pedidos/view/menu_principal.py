from .menu_base import MenuBase
from .menu_cadastro import MenuCadastro
from .menu_listar import MenuListar
from .menu_pesquisar import MenuPesquisar
from services import *


class MenuPrincipal(MenuBase):
    def __init__(self) -> None:
        super().__init__("Menu Principal", {
            "1": (self.cadastrar, "Cadastrar"),
            "2": (self.listar, "Listar"),
            "3": (self.pesquisar, "Pesquisar"),
            "4": (self.fechar_menu, "Sair")
        })
        self.produtos = ProdutoService()
        self.clientes = ClienteService()
        self.pedidos = PedidoService()
        
    def cadastrar(self) -> None:
        menu_cadastro = MenuCadastro(self.produtos, self.pedidos, self.clientes)
        menu_cadastro.interact()
    
    def listar(self) -> None:
        menu_listar = MenuListar(self.produtos, self.pedidos, self.clientes)
        menu_listar.interact()
    
    def pesquisar(self) -> None:
        menu_pesquisar = MenuPesquisar(self.produtos, self.pedidos, self.clientes)
        menu_pesquisar.interact()