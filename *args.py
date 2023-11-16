"""
args - Argumentos não nomeados

* - *args (empacotamento e desempacotamento)
"""

x, y, *resto = 1,2,3,4
print(x,y,resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_9 = soma(1,2,3,4,5,6,7,8,9)
print(soma_1_9)


# numeros = 1,2,3,4,5,6,78,89,20
# outra_soma = soma(numeros) # isso resultam em uma tupla dentro de outra tupla na função
# print(outra_soma)


numeros = 1,2,3,4,5,6,78,89,20
outra_soma_2 = soma(*numeros) # Desempacota a tupla na variável como parâmetro 
print(outra_soma_2)