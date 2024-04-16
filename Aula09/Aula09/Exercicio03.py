from random import randint
dado = []
for i in range(6001):
   dado.append(randint(1, 6))

a = dado.count(1)
b = dado.count(2)
c = dado.count(3)
d = dado.count(4)
e = dado.count(5)
f = dado.count(6)

print(f"O número 1 caiu {a} vezes")
print(f"O número 2 caiu {b} vezes")
print(f"O número 3 caiu {c} vezes")
print(f"O número 4 caiu {d} vezes")
print(f"O número 5 caiu {e} vezes")
print(f"O número 6 caiu {f} vezes")
print()
a = (a / 6000) * 100
b = (b / 6000) * 100
c = (c / 6000) * 100
d = (d / 6000) * 100
e = (e / 6000) * 100
f = (f / 6000) * 100

print(f"O número 1 caiu com frequência {a:6.2f}%")
print(f"O número 2 caiu com frequência {b:6.2f}%")
print(f"O número 3 caiu com frequência {c:6.2f}%")
print(f"O número 4 caiu com frequência {d:6.2f}%")
print(f"O número 5 caiu com frequência {e:6.2f}%")
print(f"O número 6 caiu com frequência {f:6.2f}%")