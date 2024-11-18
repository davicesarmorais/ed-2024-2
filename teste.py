class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError("Nome inválido")
        
        self.__nome = nome
    
    @idade.setter
    def idade(self, idade: int) -> None:
        if idade < 0:
            raise ValueError("Idade inválida")
        
        self.__idade = idade
        
        
