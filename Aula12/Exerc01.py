def verificar_par(n):
    if (n % 2) == 0:
        return "V"
    return "f"


x = int(input("Digite um número para verificação de impar ou par: "))
print(verificar_par(n))