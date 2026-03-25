n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >=7:
    print(f'Parabéns! você foi aprovado com média {m:.2f}')
else:
    print(f'Se esforce mais na próxima! você foi reprovado. média: {m:.2f}')