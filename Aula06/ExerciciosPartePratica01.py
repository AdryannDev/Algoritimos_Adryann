x = int(input('Coloque o número: '))
y = x % 5
z = x % 3

if y == 0 and z == 0:
    print('O valor é divisivel por 3 e 5')
else:
    print('O valor não é divisivel por 3 e por 5')