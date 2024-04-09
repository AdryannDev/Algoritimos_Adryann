v = 0
frase = input("Escreva uma frase: ")
for letra in frase:
    if letra.upper() in "AEIOU":
        v = v+1
print(f"a frase possuí {v} vogal(is)!")