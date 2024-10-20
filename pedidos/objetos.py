import datetime

class Usuario:
    def __init__(self, cpf: str, nome: str, email: str, senha: str):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha

class Produto:
    def __init__(self, nome: str, descricao: str, preco: float):
        self.id = None
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        
class Pedido:
    def __init__(self, cpf: str, produtos: list, total_pedido: float):
        self.id = None
        self.cpf = cpf
        self.produtos = produtos
        self.total_pedido = total_pedido
        self.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")