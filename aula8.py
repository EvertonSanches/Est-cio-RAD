#from math import trunc

#num = int(input("Digite um numero: "))
#raiz = sqrt(num)
#print(f"A raiz quadrada de {num} é {floor(raiz):.2f}")

#import emoji

#print(f"Olá mundo 😎")
#Exercicío16

#numr = float(input("Digite um numero real: "))
#print (f'O número digitado equivale a {trunc(numr)} Quando convertido para um número inteiro.')

#Exercício17

#co = float(input('Digite o valor do cateto oposto: '))
#ca = float(input('Digite o valor do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa vai medir: {hi:.2f}')
##Resolução com importação

#from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = hypot(co, ca)
#print(f'A hipotenusa vai medir {hi:.2f}')

#Exercício18


#mport math
#angulo = float(input('Digite o ângulo que voce deseja: '))
#seno = math.sin(math.radians(angulo))
#print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
#cosseno = math.cos(math.radians(angulo))
#print(f'O ãngulo de {angulo} tem a cosseno de {cosseno:.2f}')
#tangente = math.tan(math.radians(angulo))
#print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')

#Exercicío19
#import random
#n1 =str(input('Primeiro Aluno: '))
#n2 = str(input('Segundo Aluno: '))
#n3 = str(input('Terceiro Aluno: '))
#n4 = str(input('Quarto Aluno: '))
#lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)
#print(f"O aluno escolhido foi {escolhido}")

#import random
#n1 = str(input('Primeiro Aluno: '))
#n2 = str(input('Segundo Aluno: '))
#n3 = str(input('Terceiro Aluno: '))
#n4 = str(input('Quarto Aluno: '))
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)
#print(f'A ordem de apresentação será')
#print(lista)