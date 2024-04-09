while True:
    idade = input("Coloque sua idade: ")
    if idade.isdigit():
        idade = int(idade)
        print(f"Você tem {idade} anos de idade")
        break
    else:
        print("Insira apenas números")