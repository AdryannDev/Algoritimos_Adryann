data = input('Digite uma data <DD/MM/AAAA>: ')
dia = data[0:2:1]
mes = data[3:5:1]
ano = data[6:10:1]
data_nova = ano+mes+dia
print(data_nova)