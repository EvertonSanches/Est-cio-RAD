from rich import print
from rich.panel import Panel

class Produto:
    """
    Cria produtos adicionando nele nome e preço

    para criar um produto use:
    variavél = Produto(nome, preço)
    """
    def __init__(self, nome, preco): #Metodo Construtor
        self.nome = nome
        self.preco = preco
    def __str__(self): #Metodos de instâncias
        return f"{self.nome} custa R${self.preco:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo,title="Produto", width=34)
        print(etiqueta)

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
print(p1)
p1.etiqueta()
p2 = Produto("Notebook Gamer", 8_000)
p2.etiqueta()