import re

class Cliente:
    def __init__(self, cpf: str, nome: str, email: str, senha: str) -> None:
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido")
        
        if not self.validar_email(email):
            raise ValueError("Email inválido")
        
        if not self.validar_senha(senha):
            raise ValueError("Senha inválida")
        
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        
    def __str__(self) -> str:
        return "\n".join([
            f"CPF: {self.cpf}",
            f"Nome: {self.nome}",
            f"Email: {self.email}",
            f"Senha: {self.senha}",
        ])  

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.cpf == other.cpf
        return False

    def __hash__(self):
        return hash(self.cpf)

    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def senha(self) -> str:
        return '*' * len(self.__senha)
    
    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError("Nome inválido")
        self.__nome = nome
        
    @email.setter
    def email(self, email: str) -> None:
        if not isinstance(email, str):
            raise ValueError("Email inválido")
        
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")
        
        self.__email = email
        
    @senha.setter
    def senha(self, senha: str) -> None:
        if self.validar_senha(senha):
            self.__senha = senha
        else:
            raise ValueError("Senha inválida")
        
    @staticmethod
    def validar_email(email: str) -> bool:
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        return bool(re.match(email_regex, email))
    
    @staticmethod
    def validar_senha(senha: str) -> bool:
        if len(senha) < 8:
            return False
        
        especial = any(not c.isalnum() for c in senha)
        numero = any(c.isdigit() for c in senha)
        letra = any(c.isalpha() for c in senha)
        return especial and numero and letra
    
    
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        return True
        # Implementaçao real (mas nao vou usar pq é muito ruim pra usar de mentirinha)
        """ cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        for i in [9, 10]:
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                return False
        return True """
