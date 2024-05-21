def ePrimo():
    global g
    t = 2
    a = x / t
    if x == 2:
        b = (True)
    else:
        for i in range(x - 2):
            y.append(a)
            if y[i] != int(y[i]):
                z = True
            else:
                z = False
            w.append(z)
            t = t + 1
            a = x / t
    if all(w) == True:
        b = True
    else:
        b = False
    if b == True:
        g = "o número é primo."
        print(g)
    else:
        g = "o número não é primo."
        print(g)


def numeroAte():
    global x, d, f
    ePrimo()
    c = 0
    d = x
    for i in range(len(w)):
        x = f
        ePrimo()
        if g == "o número é primo.":
            c += 1
        f += 1
    print(f"até o número {d} existem {c} números primos.")


def menu1():
    print('''
        1- O número é primo?
        2- Quantos números primos tem até o número...
        3- Sair.''')


x = ""
y = []
z = False
w = []
a = 0
menu = 0
t = 0
c = 0
d = x
e = True
f = 2
g = ""
while menu == 0:
    menu1()
    opcao = input("Escolha uma das opções: ")
    if opcao == "1":
        x = int(input("Digite um número: "))
        ePrimo()
    elif opcao == "2":
        x = int(input("Digite um número: "))
        numeroAte()
    elif opcao == "3":
        menu = 1
    else:
        print("esta, não é uma opção, tente novamente.")
