# Entendendo os seus próprios módulos Python
# O primeiro módulo executado se chama __main__

# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.

# Ele não reconhece pastas e módulos acimda do __main__ por
# padrão

# O python conhece todos os módulos e pacortes presentes
# nos caminhos de sys.path

import sys

print('Este módulo se chama ', __name__)
print(sys.path)

# Os módulos são singletons - apenas uma instância é carregada

# import importlib
# importlib.reload('nome_do_módulo') # recarrega o módulo
