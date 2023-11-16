# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

print(dc)

s1 = {i for i in range(10)}

print(s1)