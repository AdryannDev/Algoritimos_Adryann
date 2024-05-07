import math
def area_circulo(raio):
    area = math.pi * pow(raio, 2)
    return area

r = float(input("Digite o raio: "))
print(f"A area do círculo de raio {r} é igual a {area_circulo(r)}")