from .menu_base import MenuBase
from .menu_cadastro import MenuCadastro
from .menu_listar import MenuListar
from .menu_pesquisar import MenuPesquisar
from services import *


class MenuPrincipal(MenuBase):
    def __init__(self, contexto: Contexto) -> None:
        opcoes = {
            "1": (self.cadastrar, "Cadastrar"),
            "2": (self.listar, "Listar"),
            "3": (self.pesquisar, "Pesquisar"),
            "4": (self.fechar_menu, "Sair")
        }
        
        super().__init__("Menu Principal", opcoes, contexto)
        
    def cadastrar(self) -> None:
        menu_cadastro = MenuCadastro(self.contexto)
        menu_cadastro.interact()
    
    def listar(self) -> None:
        menu_listar = MenuListar(self.contexto)
        menu_listar.interact()
    
    def pesquisar(self) -> None:
        menu_pesquisar = MenuPesquisar(self.contexto)
        menu_pesquisar.interact()