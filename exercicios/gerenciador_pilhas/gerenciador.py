from pilha import Stack

class GerenciadorPilhas:
    def __init__(self):
        self.__atual_indice = 0
        self.__pilhas = []
    
    @property
    def atual(self):
        return self.__pilhas[self.__atual_indice]
    
    @atual.setter
    def atual(self, index):
        if index <= 0 or index > len(self.__pilhas):
            raise IndexError("Index out of range")
        self.__atual_indice = index - 1
    
    @property
    def atual_indice(self):
        return self.__atual_indice
    
    def __str__(self) -> str:
        if len(self.__pilhas) == 0:
            return "Nenhuma pilha selecionada"
        
        return "\n".join([
            f"Pilha selecionada: {self.__atual_indice + 1} de {len(self.__pilhas)}",
            str(self.__pilhas[self.__atual_indice])
        ])
        
    def nova_pilha(self, pilha = None):
        if pilha is None:
            self.__pilhas.append(Stack())
        else:
            self.__pilhas.append(pilha)
        
    def remove(self, index):
        try:
            self.__pilhas.pop(index)
            if self.__atual_indice >= len(self.__pilhas):
                self.__atual_indice -= 1
        except IndexError:
            print("Pilha inexistente")
    
    def buscar_pilha(self, index):
        try:
            return self.__pilhas[index]
        except IndexError:
            print("Pilha inexistente")
    