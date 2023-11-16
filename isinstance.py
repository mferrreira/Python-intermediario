# isinstance - para saber se o objeto é de determinado tipo (typeof)

lista = [
    'a', 1, 1.1, True, [0,1,2], {0,1}, (1,2), {'nome': 'marcio'}
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print('STR')
        print(item.upper())
    
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item ** 2)

    else:
        print('OUTRO')
        print(item)