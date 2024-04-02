idade = 100
soma = 0
qtd = 0
while idade > 0:
    idade = int(input(f'Coloque a idade {qtd +1} : '))
    if idade > 0:
        soma = soma + idade
        qtd = qtd + 1
media = soma/qtd
print(f"A média das {qtd} idades é: {round(media)} anos")