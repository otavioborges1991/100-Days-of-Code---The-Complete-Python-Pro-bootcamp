# Target is the number up to which we count
dicionario = [
    {'nome': 'Otavio', "idade": 33},
    {'nome': 'Larissa', "idade": 35},
]

for pessoa in dicionario:
    if pessoa['nome'] == 'Otavio':
        pessoa['nome'] = 'Jose'
    if pessoa['idade'] == 35:
        pessoa['idade'] = 36
    print(pessoa)