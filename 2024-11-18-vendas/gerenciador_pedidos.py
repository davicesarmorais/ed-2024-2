from pedido import Pedido

class GerenciadorPedidos:
    def __init__(self):
        self.__repositorio_pedidos = {}

    def __str__(self)->str:
        return "\n".join([
            f'ID PEDIDO: {id_pedido}\n{pedido.__str__()}'
            for id_pedido, pedido in self.repositorio_pedidos.items()
        ])
            
    def __len__(self)->int:
        return len(self.repositorio_produtos)
        
    @property
    def repositorio_pedidos(self):
        return self.__repositorio_pedidos
    
    def adicionar(self, pedido: Pedido):
        self.repositorio_pedidos[pedido.id] = pedido

    def pesquisar(self, id: int) -> Pedido:
        return self.repositorio_pedidos.get(id)
    
    def remover(self, id: int) -> Pedido:
        return self.repositorio_pedidos.pop(id, None)
