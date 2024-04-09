frase = input("digite uma frase: ").strip()
fraseDividida = frase.split()
n = 0
fraseSemEspaco = ''
for frase in fraseDividida:
    palavra = fraseDividida[n]
    fraseSemEspaco = fraseSemEspaco + palavra
    n = n + 1
fraseInvertida = fraseSemEspaco[::-1]
if fraseSemEspaco == fraseInvertida:
    print("a frase é um palindromo!")
else:
    print("a frase não é um palindromo!")