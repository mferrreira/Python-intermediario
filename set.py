# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática

# São representados graficamente pelo digrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

# Criando um set
# set(iterável) ou {1,2,3}

s1 = set()
print(s1, type(s1))

# Sets são eficientes para remover valores duplicados de iteráveis.
#    - seus valores são sempre únicos
#    - não aceitam valores mutáveis
#    - eles não têm índices
#    - eles não garantem ordem
#    - eles são iteráveis (for, in, not in )

lista1 = [1,2,3,4,4,4,4,4,4,4,4,4,1]
set1 = set(lista1)  # remove os itens duplicados
lista2 = list(set1) # tranforma a estrutura novamente em uma lista
print(lista2)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('marcio') # add recebe apenas um valor
s1.add(1)
s1.update(('Olá mundo')) # pode ser usado para enviar vários valores, mas é necessário encapsular em uma tupla
# s1.clear() limpa o set
s1.discard('marcio') # remove o item do set

# Operadores úteis:
# união | união (union) - Une
# Intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes paenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s5 = s1 ^ s2

print(s3)
print(s4)
print(s5)

# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        print('VOCE ACHOU A LETRA SECRETA')
        break
    print(letras)