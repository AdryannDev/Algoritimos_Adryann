def potencia(base,expoente=2):
    """Função que calcula a potência de um número.
    Valor de Entrada:
    base = número elevado a ser calculado(base);
    expoente = número que irá ser o expoente(expoente);
    resultado = pow(base, expoente);"""

    resultado = base ** expoente
    return resultado

n = float(input("Digite a base: "))
e = int(input("Expoente: "))
print(f"Valor com expoente: {potencia(n,e)}")
print(f"Valor completo: {potencia(n)}")

print(help(potencia))