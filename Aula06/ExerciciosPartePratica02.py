a = int(input('Insira o valor: '))

if a < 1001:
    b = a * 0.1
    print('o desconto é:', b)
    print('valor total é:', a-b)
elif 1000 < a < 5000:
    b = a * 0.2
    print('o desconto é:', b)
    print('valor total é:', a - b)
else:
    b = a * 0.3
    print('o desconto é:', b)
    print('valor total é:', a - b)