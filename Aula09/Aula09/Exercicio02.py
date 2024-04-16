lista = []
for i in range(5):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)

maxLista = max(lista)
minLista = min(lista)

print(f"---------------------------------")
print(f"Valor maximo: {maxLista}, sua posição: [{lista.index(maxLista)}]")
print(f"Valor minimo: {minLista}, sua posição: [{lista.index(minLista)}]")
print(f"---------------------------------")