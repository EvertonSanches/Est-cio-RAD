class Gafanhoto:
    def __init__(self): # Metodo Construtor
        # Atributo de Instância
        self.nome = ""
        self.idade = 0


        # Metodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Everton"
g1.idade = 26
g1.aniversario()
print(g1.mensagem())