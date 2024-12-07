from services import *

class Contexto:
    def __init__(self):
        self.produtos = ProdutoService()
        self.pedidos = ProdutoService()
        self.clientes = ClienteService()