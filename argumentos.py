"""
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

Argumento: valores na chamada da função
Parâmetro: variáveis na definição da função
"""

def soma(x,y,z):
    #definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1,2,3)
soma(1,y=2,z=6)