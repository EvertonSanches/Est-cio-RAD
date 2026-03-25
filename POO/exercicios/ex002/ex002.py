#Declaração da Classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Metodo Construtor
        # Atributo de Instância
        self.nome = nome
        self.idade = idade


        # Metodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
# Declaração de Objetos
g1 = Gafanhoto("Everton", 26)
g1.aniversario()
#print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method | Metodo possui () no final, atributo não possui.
print(g1.__class__) # Para descobrir de qual classe é esse objeto.

g2 = Gafanhoto("Maria", 36)
g2.aniversario()
print(g2)
print(g2.__getstate__())


#print(g3.__doc__) # Dunder Attribute