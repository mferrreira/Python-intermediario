# Execício - Adiando execução de funções

def soma(x,y):
    return x + y

def multiplica(x, y):
    return x * y

def cria_funcao(funcao, *args):
    def executa(x):
        return funcao(x, *args)
    return executa

soma_com_cinco = cria_funcao(soma, 5)
multiplica_por_dez = cria_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(2))