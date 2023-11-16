"""
Exercícios com funções

Crie uma função que multiplica todos o sargumentos não nomeados recebidos
retorne o total para uma variável e mostre o valor da variável.

Cria uma função falar se um número é par ou ímpar.
Retorne se o número é par ou ímpar
"""

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def parOuImpar(numero):
    return 'O número é par' if numero % 2 == 0 else 'O número é impar'

valor = multiplica(1,4,12,54,3,6,7,1,34,9)
print(valor)

print(parOuImpar(1))
print(parOuImpar(0))
print(parOuImpar(2))