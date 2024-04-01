frase = input("Digite uma frase: ").upper()
qtdA = 0
for caracterA in frase:
    if caracterA == "A":
        qtdA = qtdA + 1
print(f'A quantidade de "As" é {qtdA}')