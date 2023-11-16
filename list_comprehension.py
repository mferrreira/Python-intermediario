# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis

lista = []

for numero in range(10):
    lista.append(numero)


lista = [numero * 2 for numero in range(10)]
print(lista)


produtos = [
    {'nome':'p1', 'preco':10},
    {'nome':'p2', 'preco':20},
    {'nome':'p3', 'preco':30},
    {'nome':'p4', 'preco':40},
]

novos_produtos = [produto['nome'] for produto in produtos]

# ANTES DO FOR:     Mapeamento
# DEPOIS DO FOR:    Filtro / condicional

novos_produtos = [ { **produto, 'preco': produto['preco'] * 1.05 } if produto['preco'] > 20 else{**produto} for produto in produtos if produto['preco'] > 10 and produto['preco'] >= 20 ]

print(novos_produtos)

lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]

print(lista)

lista = [
    [(x,letra) for letra in 'Márcio']
    for x in range(3)
]

print(lista)