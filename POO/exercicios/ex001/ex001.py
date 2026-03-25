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

g2 = Gafanhoto()
g2.nome = "Maria"
g2.idade = 46
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = "Robson"
g3.idade = 33
g3.aniversario()
g3.aniversario()
print(g3.mensagem())