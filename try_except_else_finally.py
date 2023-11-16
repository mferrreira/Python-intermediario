# try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')

print()

# Finally - Sempre será executado

try:
    print(1)
    # open
    7/0

except ZeroDivisionError as error:
    print('Erro:', error.__class__.__name__)

else:
    print('Não deu erro')

finally:
    print('Fechar arquivo')

