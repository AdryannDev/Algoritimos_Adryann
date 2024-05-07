def e_primo():
    if a == (1 or 2):
        print("É primo")
    else:
        if (a/2)-int(a) == 0:
            print("É primo")
        else:
            print("Não é primo")


a = int(input("Digite um número: "))

print(e_primo())