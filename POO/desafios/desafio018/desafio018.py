class Churrasco:
    """

    """
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def __str__(self):
        return f"O {self.titulo} com {self.quant} convidados vai precisar de: "

    def analisar(self):


c1 = Churrasco("Churasquin",5)

print(c1)