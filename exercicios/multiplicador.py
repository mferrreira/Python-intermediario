"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o
número recebido como parâmetro
"""

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(4))
print(triplicar(3))
print(quadruplicar(10))