from produto import Produto

class GerenciadorProdutos:
    def __init__(self):
        self.__repositorio_produtos = {}

    def __str__(self)->str:
        return f"\n{'-' * 20}\n".join([
            produto.__str__() for produto in self.repositorio_produtos.values()
        ])
            
    def __len__(self)->int:
        return len(self.repositorio_produtos)
        
    @property
    def repositorio_produtos(self):
        return self.__repositorio_produtos
    
    def adicionar(self, produto: Produto):
        self.repositorio_produtos[produto.id] = produto

    def pesquisar(self, id: int) -> Produto:
        return self.repositorio_produtos.get(id)
    
    def remover(self, id: int) -> Produto:
        return self.repositorio_produtos.pop(id, None)
