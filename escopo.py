"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos
A palavra global faz uma variável do escopo externo
ser a mesma no escopo interno (má prática)
"""

x = 1 # escopo global

def escopo():
    global x # acesso ao x global
    
    x = 10 # escopo local (x != x)
    
    print(x)

    def outra_funcao():
        x = 11
        print(x)
    
    outra_funcao()

print(x)
escopo()
print(x)

# outra_funcao() fora do escopo