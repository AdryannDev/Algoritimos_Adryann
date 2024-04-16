from random import randint

m = []
l = []

for y in range(5):
    for x in range(5):
        l.append(randint(1, 100))
    m.append(l)
    l = []
print(m)
soma = 0
h = 0
for i in range(0,5,2):
    for j in range(0,5,1):
        h = h + m[i][j]
    soma = m[i]
    print(soma)
print(f"{soma=}")