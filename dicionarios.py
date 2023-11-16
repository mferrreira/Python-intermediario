"""
Dicionários em Python (tipo dict)

Dicionários são estruturas de dados do tipo 
par de "chave" e "valor".
Chaves podem ser consideradas como o "índide"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.

Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list

pessoa {
    'nome': 'Márcio Martins',
    'sobrenome': 'Ferreira',
    'idade': 21,
    'altura': 1.66,
    'enderecos': [
        {'rua': 'Rua 4', 'numero': 195},
        {'rua': 'Travessa Marechal Dutra', 'numero': 28}
    ]
}

"""

pessoa = {
    'nome': 'Márcio Martins',
    'sobrenome': 'Ferreira',
    'idade': 21,
    'altura': 1.66,
    'enderecos': [
        {'rua':'Rua 4', 'numero': 195},
        {'rua':'Travessa Marechal Dutra', 'numero': 28}
    ]
}

print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print(f'\n' + '*' * 30 + '\n')

for chave in pessoa:
    print(chave, pessoa[chave])