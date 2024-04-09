nome = input('digite seu nome completo: ')
nascimento = input('digite sua data de nascimento <DD/MM/AAAA>: ')
data = nascimento.split('/')

palavras = nome.split()
pre_nome = palavras[0]
sobrenome = palavras[1]

print(f"Olá sr(a).{sobrenome} muito bonito seu nome: {pre_nome}")
print(f"Você nasceu no dia {data[0]} e no mês {data[1]}")