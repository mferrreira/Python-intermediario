"""
Closure e funções que retornam funções
"""


"""
    # Closures: Adiar a execução de uma função

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}'
        return saudar # sem parenteses, retorna a função, não o seu valor

    s1 = criar_saudacao('Bom dia', 'Marcio')
    s2 = criar_saudacao('Boa noite', 'Marcio')

    print(s1)   # Passos da função, sem executar
    print(s2()) # Variável a que foi atribuída a função e executada, ou seja, closure


"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar # retorna o escopo atual

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

nomes = ['Marcio', 'flavia', 'ana', 'kim']

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))