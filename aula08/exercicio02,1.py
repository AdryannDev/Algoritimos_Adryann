data = input('Digite uma data <DD/MM/AAAA>: ')
data_separada = data.split('/')
dia = data_separada[0]
mes = data_separada[1]
ano = data_separada[2]
data_nova = ano+mes+dia
print(data_nova)