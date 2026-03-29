from rich import print
from rich.panel import Panel


class Churrasco:
    """

    """

    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82.40


    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} participantes."


    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float :
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados [/]"
        conteudo += (f"\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg "
                     f"custa R${Churrasco.preco_kg}")
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada participante ira pagar [yellow]R${self.calcular_custo_individual():,.2f}[/]"
        painel = Panel (conteudo, title=self.titulo)
        print(painel)


c1 = Churrasco("Churasquin",35)
c2 = Churrasco("Churas-rock", 40)
c1.analisar()
c2.analisar()