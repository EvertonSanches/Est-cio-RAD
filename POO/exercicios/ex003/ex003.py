from rich import print
from rich import inspect
#Classe:
class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
Para criar uma conta, use:
variavel = ContaBancaria (id, nome, saldo)

    """
    def __init__(self, id, nome, saldo = 0): #Metodo Construtor
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")
    def __str__(self): #Metodos de Instância
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de Saldo"

    def depositar(self,valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Não foi possivel realizar o saque, saldo atual R${self.saldo:,.2f}, valor solicitado {valor:,.2f}")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
#Uso do Objeto:
c = ContaBancaria(111, "Jose", 500)
#c1 = ContaBancaria(112, "Everton", saldo=3000)
#c1.depositar(500)
#c1.sacar(3550)
#print(c1)



