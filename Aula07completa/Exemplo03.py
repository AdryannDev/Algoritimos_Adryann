frase = input("Digite uma frase: ").upper()
qtd = 0
for caracter in frase:
    if caracter in 'AEIOUÃÕÁÉÍÓÚÀÜ':
        qtd = qtd + 1
print(f'A quantidade de vogais é {qtd}')