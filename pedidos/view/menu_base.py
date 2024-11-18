from utils.utils import limpar_tela
from services.contexto import Contexto

class MenuBase:
    def __init__(self, titulo: str, opcoes: dict, contexto: Contexto) -> None:
        self.titulo = titulo
        self.opcoes = opcoes
        self.contexto = contexto
        self.__running = True
    
    def interact(self) -> None:
        while self.__running:
            limpar_tela()
            print(self)
            opcao = input("Escolha uma opção: ")
            if opcao in self.opcoes:
                self.opcoes[opcao][0]()
        
        self.__running = True
    
    def fechar_menu(self) -> None:
        self.__running = False
        
    def __str__(self) -> str:
        opcoes_str = '\n'.join(f"{key}. {val[1]}" for key, val in self.opcoes.items())
        return f"-- {self.titulo} --\n{opcoes_str}"
