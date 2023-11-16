"""
Highet Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):

    # é possível retornar funções dentro de funções
    return funcao(*args)


                    # é possível passar funções como parâmetro
print(  executa(    saudacao, 'bom dia', 'marcin'   ))
print(  executa(    saudacao, 'bom dia', 'fravinha' ))
