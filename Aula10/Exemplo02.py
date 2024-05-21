
filmes = {
    "avatar": 2009,
    "titanic": 1997,
    "starwars": 2015,
    "harry-potter": 2011,
    "avengers": 2012
}
print(filmes.items())
# print(filmes.keys())
# print(filmes.values())
# for chave, valor in filmes.items():
#     print(f"Assisti a {chave.upper()} lançado em {valor}")
filmes.update({"frozen": 2013})
print(filmes)