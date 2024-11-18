class Produto:
    def __init__(self, id_produto: int, descricao: str, preco: float):
        if not self.validar_id(id_produto):
            raise ValueError("ID inválido")
        if not self.validar_descricao(descricao):
            raise ValueError("Descricão inválida")
        if not self.validar_preco(preco):
            raise ValueError("Preço inválido")
        
        self.__id = id_produto
        self.__descricao = descricao
        self.__preco = preco
    
    def __str__(self) -> str:
        return "\n".join([
            f"ID: {self.id}",
            f"Descricao: {self.descricao}",
            f"Preco: {self.preco:.2f}",
        ])  

    def __eq__(self, other) -> bool:
        if isinstance(other, Produto):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id) 
           
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def descricao(self) -> str:
        return self.__descricao.capitalize()
    
    @property
    def preco(self) -> float:
        return round(self.__preco, 2)
    
    @id.setter
    def id(self, id_produto: int):
        if not self.validar_id(id_produto):
            raise ValueError("ID inválido")
        
        self.__id = id_produto
        
    @descricao.setter
    def descricao(self, descricao: str):
        if self.validar_descricao(descricao):
            raise ValueError("Descricão inválida")
        
        self.__descricao = descricao
        
    @preco.setter
    def preco(self, preco: float):
        if not self.validar_preco(preco):
            raise ValueError("Preço inválido")
        
        self.__preco = preco
        
    @staticmethod
    def validar_preco(preco: float) -> bool:
        return isinstance(preco, float) or preco < 0
        
    @staticmethod
    def validar_id(id_produto: int) -> bool:
        return isinstance(id_produto, int)
        
    @staticmethod
    def validar_descricao(descricao: str) -> bool:
        return not isinstance(descricao, str) or len(descricao) <= 50