from produto import Produto
from datetime import datetime


class Carrinho:
    def __init__(self) -> None:
        self.__carrinho = {}

    def __len__(self) -> int:
        return len(self.__carrinho)

    @property
    def carrinho(self) -> dict:
        return self.__carrinho
    
    def __str__(self) -> str:
        return f'\n{"-"*20}\n'.join([
            f'{produto.__str__()}\nQuantidade: {qtd}' 
            for produto, qtd in self.carrinho.items()
        ])
    
    def adicionar(self, produto: Produto, qtd_itens: int) -> None:
        if qtd_itens < 0:
            raise ValueError("Quantidade nao pode ser negativa")
        
        if qtd_itens == 0:
            self.remover(produto)
        else:
            self.__carrinho[produto] = qtd_itens
    
    
    def remover(self, produto: Produto) -> None:
        return self.__carrinho.pop(produto, None)
        

class Pedido:
    __serial = 0
    
    def __init__(self, carrinho: Carrinho) -> None:
        Pedido.__serial += 1
        self.__id = Pedido.__serial
        self.__itens = carrinho
        self.__data = datetime.now().strftime("%d-%m-%Y")
        self.__total_pedido = sum(p.valor * qtd for p, qtd in carrinho.carrinho.items())

    def __str__(self) -> str:
        return "\n".join([
            f"ID PEDIDO: {self.id}",
            f"Data: {self.data}",
            f"Total: R$ {self.total_pedido:.2f}",
            f"------ Itens -------",
            self.itens.__str__(),
            f"---------------------"
        ])

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def total_pedido(self) -> float:
        return self.__total_pedido
    
    @property
    def data(self) -> str:
        return self.__data
    
    @property
    def itens(self) -> Carrinho:
        return self.__itens


# import random
# carrinho = Carrinho()

# nomes = ["Camiseta", "Calça", "Cueca", "Vestido", "Calça Jeans"]
# valores = [float(random.randint(50, 400)) for _ in range(len(nomes))]

# for i in range(len(nomes)):
#     produto = Produto(nomes[i], valores[i])
#     carrinho.adicionar(produto, random.randint(1, 5))

# pedido = Pedido(carrinho)

# print(pedido)

# from save import abrir_json, salvar_produtos
# from gerenciador_produtos import GerenciarProduto

# # estrutura de dados para armazenar todos pedidos
# colecao_pedidos = {} #chave=ID;valor=list(carrinho)
# # variável controladora do serial do pedido
# serial_num_pedido = 0


# # carregando dados
# dados = abrir_json()
# gerenciador = GerenciarProduto(dados)
# salvar_produtos(dados)

# def gerar_id_pedido() -> int:
#     global serial_num_pedido
#     serial_num_pedido += 1
#     return serial_num_pedido

# def fechar_pedido(colecao_pedidos:dict, carrinho:list)->int:
#     id_pedido = gerar_id_pedido()
#     colecao_pedidos[id_pedido] = carrinho
    
#     return id_pedido

# def add_produto_carrinho(carrinho:list, idProduto:int,quant:int):
#     carrinho.append([idProduto,quant])

# def exibir_pedido(carrinho:list):
#     print('======================================================')
#     print("                 Itens do pedido:")
#     print('======================================================')
#     print('idProduto  | Descrição      | Preço Unit. | Quantidade')
#     print('-----------  ---------------  ------------  ----------')
          
#     total = 0
#     for item in carrinho:
#         produto = gerenciador.pesquisar_produto(item[0])        
#         print(f"   {produto['id']:03d}       {produto['descricao']:15s}    {produto['valor']:10.2f}      {item[1]:3d}")
#         total += produto['valor'] * item[1]

#     print('======================================================')
#     print(f"Valor total das suas comprinhas:{total:.2f}")
#     print('======================================================')