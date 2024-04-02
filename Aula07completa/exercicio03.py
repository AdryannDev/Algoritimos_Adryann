somaPeso = 0
somaAltura = 0
IMC_minimo = 100
IMC_maximo = 0
for a in range(1, 6):
    peso = float(input(f"insira o peso da pessoa {a} em Kg: "))
    altura = float(input(f"insira a altura da pessoa {a} em M: "))
    somaPeso = somaPeso + peso
    somaAltura = somaAltura + altura
    IMC = peso / (altura**2)
    if IMC > IMC_maximo:
        IMC_maximo = IMC
    if IMC < IMC_minimo:
        IMC_minimo = IMC
mediaPeso = somaPeso / 5
mediaAltura = somaAltura / 5
print(f"A média de massa é: {mediaPeso}")
print(f"A média de altura é: {mediaAltura}")
print(f"O IMC maximo é: {IMC_maximo}")
print(f"O IMC minimo é: {IMC_minimo}")