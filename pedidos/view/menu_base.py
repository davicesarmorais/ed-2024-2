from utils.utils import limpar_tela

class MenuBase:
    def __init__(self, titulo: str, opcoes: dict = {}) -> None:
        self._titulo = titulo
        self._running = True
        self._opcoes = opcoes
        
    def interact(self) -> None:
        while self._running:
            limpar_tela()
            print(self)
            opcao = input("Escolha uma opção: ")
            if opcao in self._opcoes:
                self._opcoes[opcao][0]()
        
        self._running = True
    
    def fechar_menu(self) -> None:
        self._running = False
        
    def __str__(self) -> str:
        opcoes_str = '\n'.join(f"{key}. {val[1]}" for key, val in self._opcoes.items())
        return f"-- {self._titulo} --\n{opcoes_str}"
