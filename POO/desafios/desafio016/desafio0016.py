from rich import print
from rich import emoji
class Funcionario:
    """
Cria um funcionário possuindo nome, setor e cargo
Para criar um funcionário, use:
variavel = Funcionario(nome, setor, cargo)
    """
    def __init__(self, nome, setor, cargo): #Metodo Construtor
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self): #Metodos de instâncias
        return f":handshake: Olá, sou [blue]{self.nome}[/] e trabalho no setor de {self.setor} como {self.cargo} na empresa LTDE"

f1 = Funcionario("Everton", "TI", "Desenvolver Junior")
f2 = Funcionario("Maria", "Marketing", "Diretora de marketing")
print(f1.apresentacao())
print(f2.apresentacao())


