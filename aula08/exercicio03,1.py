frase = input("Escreva uma frase: ").lower()
vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
print(f"a frase possuí {vogais} vogal(is)!")