n = int(input('Insira o valor de n: '))
e = 0
k = 1
while k <= n:
    e = e + (2 ** k)
    k = k + 1
print(f'O resultado é: {e}')
