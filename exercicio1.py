#def saudacao(nome: str) -> str:
#    return f"Olá, {nome}! Seja bem-vindo(a)!"

#nome_usuario = input("Informe seu nome: ")
#mensagem = saudacao(nome_usuario)
#print(mensagem)

#def calcular_media(n1: float, n2: float, n3: float) -> str:
#    media = (n1 + n2 + n3) / 3
#    return media
#def verificar_aprovacao(media: float) -> str:
#    if media >= 7.0:
#        return "Aprovado"
#    else:
#        return "Reprovado!"
#nota1 = 8.6
#nota2 = 6.0
#nota3 = 7.5
#media_final = calcular_media(nota1, nota2, nota3)
#resultado = verificar_aprovacao(media_final)
#print(f"Média:{media_final:.2f} - Resultado: {resultado}")

def calcular_preco_final(valor_produto:float) -> float:
    if valor_produto > 100:
        return valor_produto - (valor_produto/10)
    else:
        return valor_produto
num=float(input("Valor do produto: "))
resultado = calcular_preco_final(num)
print(resultado)