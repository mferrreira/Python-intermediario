# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90}
]

import copy
copiar = copy.deepcopy

novos_produtos = [ {produto['nome']: produto['preco'] * 1.1} for produto in copiar(produtos) ]

# Ordene os produtos por nome descrescento (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_odenadors_por_nome = sorted(copiar(produtos), key=lambda item: item['nome'], reverse=True)

# Ordene os produtos por preco crescendo (do menos para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_odenadors_por_preco = sorted(copiar(produtos), key=lambda item: item['preco'])

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_odenadors_por_nome, sep='\n')
print()
print(*produtos_odenadors_por_preco, sep='\n')