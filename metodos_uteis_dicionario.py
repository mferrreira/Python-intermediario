"""
Métodos úteis dos dicionários em Python

len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma cahve
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro

"""


# Deep copy e Shallow Copy:

d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1 # não copia a estrutura, mas aponta pro mesmo endereço de memória

d2 = d1.copy()
print(d2)

d2['l1'] = [1,2,3]
print(d2)

d3 = d2.copy() # Tipos mutáveis (list / dict) serão apontados pelos dois dicionários

d3['l1'][1] = 'a'

print(d2) # 'l1': [1,'a',3]