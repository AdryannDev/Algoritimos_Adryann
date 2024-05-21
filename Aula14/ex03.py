z = 1
y = 0
x = input("Digite o RA: ")
for i in range(len(x)):
    y += int(x[i])
    z *= int(x[i])
print(f"a soma dos digitos do RA é {y} e a multiplicação é {z}.")