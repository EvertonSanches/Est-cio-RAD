# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# n3 = float(input("Digite a terceira nota: "))

# soma = n1 + n2 + n3
# media = soma / 3

# if media >= 7.0:
#     print(f"Média: {media:.2f} - Aprovado")
# else:
#     print(f"Média: {media:.2f} - Reprovado")

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# peso = float(input("Digite seu peso: "))

# print("Olá", nome, "Você tem", idade, "anos e pesa", peso, "kg.")

# dia = int(input("Digite o dia do seu nascimento: "))
# mes = (input("Digite o mês do seu nascimento: "))
# ano = int(input("Digite o ano do seu nascimento: "))

# print("Você nasceu em", dia, "de", mes, "de", ano)

#primeiro_numero = int(input("Digite o primeiro número: "))
#segundo_numero = int(input("Digite o segundo número: "))

#soma = primeiro_numero + segundo_numero

#resultado = soma

#print("A soma entre", primeiro_numero, "e", segundo_numero, "é", resultado)

#nome = input("Qual seu nome? ")
#print("Prazer em te connhecer, {}!" .format(nome))

#Exercício05:

#valor = int(input("Digite um valor: "))
#print("Analisando o valor {}, o seu antecessor é {}, e o seu sucessor é {}".format(valor, valor-1, valor+1))

#Exercício06
#num = int(input("Digite um numero: "))


#print("o dobro de {} vale {}".format(num, (num*2)))
#print("o triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(num, (num*3), num, (num**(1/2))))

#Exercicio07

#n1 = float(input("Primeira Nota do Aluno: "))
#n2 = float(input("Segunda Nota do Aluno: "))
#n3 = float(input("Terceira Nota do Aluno: "))

#media = (n1 + n2 + n3) / 3

#print("A Média Final do aluno foi de: {:.2f}".format(media))

#Exercício08:

#medida = float(input("Digite o valor em metros: "))
#cm = medida * 100
#mm = medida * 1000

#print(f'A medida de {medida} corresponde a {cm:.0f}cm e {mm:.0f}mm')

#Exercício09

#num = int(input("Digite um numero para ver sua tabuada: "))

#tabuada = num * 1
#print('-' * 18)
#print(f"{num} x 1 = {tabuada}")
#print(f"{num} x 2 = {tabuada*2}")
#print(f"{num} x 3 = {tabuada*3}")
#print(f"{num} x 4 = {tabuada*4}")
#print(f"{num} x 5 = {tabuada*5}")
#print(f"{num} x 6 = {tabuada*6}")
#print(f"{num} x 7 = {tabuada*7}")
#print(f"{num} x 8 = {tabuada*8}")
#print(f"{num} x 9 = {tabuada*9}")
#print(f"{num} x 10 = {tabuada*10}")
#print('-' * 18)

#Exercicio10:

#carteira = float(input("Quanto dinheiro você possue na carteira? R$"))

#dolar = carteira/5.20

#print(f"Com R${carteira} você pode comprar ${dolar:.2f} Dolar")

#Exercício11
#largura = float(input("Largura da parede: "))
#altura = float(input("Altura da parede: "))
#area = largura * altura
#tinta = area / 2
#print(f"sua parede tem a dimensão de {largura} x {altura} e sua area é de  {area}m², você vai precisar de {tinta}l de tinta.")

#Exercício12

#preco_produto = float(input("Valor do produto: "))
#desconto_produto = preco_produto - (preco_produto * 5 /100)

#print(f"O valor do produto de R${preco_produto} na promoção sai por {desconto_produto:.2f} com o desconto de 5%")

#Exercício13

#salario_atual = float(input("Qual salario atual do funcionario? R$"))

#aumento = salario_atual + (salario_atual * 15 /100)

#print(f"Um funcionario que ganhava R${salario_atual:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}")

#Exercício14

#celsius = float(input("Temperatura em Celsius: "))
#fahrenheit = (celsius * 1.8) + 32

def calcular_salario(salario_base: float) -> float:
    salario_atual = salario_base
    if salario_atual <= 1500:
        salario_atual = salario_atual + (salario_atual * 15/100)

    elif salario_atual <= 3000:
        salario_atual = salario_atual + (salario_atual * 10/100)

    else:
        salario_atual = salario_atual + (salario_atual * 5/100)
    return salario_atual
novo_salario= calcular_salario(1580)

print(novo_salario)



#print(f"A temperatura de ª {celsius} equivale a ª{fahrenheit}")

#dias_alugados =int(input("Quantos dias o carro foi alugado?"))
#km_dias = float(input("Quantos km foram percorridos ?"))
#dia = 60 * dias_alugados
#km = 0.15 * km_dias
#valor_total = dia + km
#print(f"Alugado por: {dias_alugados} Dias. R$60 o dia, o que dá R${dia}, Foi rodado {km_dias}KM | R$0.15 por KM, que dá {km}, total a pagar {valor_total:.2f}.")


#print(f"A temperatura de ª{celsius} equivale a ª{fahrenheit}")

