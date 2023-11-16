# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opcoes': ['1','2','3','4','5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opcoes': ['25','55','75','10','5'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opcoes': ['4','5','6','2','1'],
        'Resposta': '5'
    },
]

def perguntas_e_respostas(perguntas):
    contador_acertos = 0
    total = len(perguntas)

    for pergunta in perguntas:
        enunciado = pergunta['Pergunta']
        opcoes = pergunta['Opcoes']
        resposta_correta = pergunta['Resposta']

        print(enunciado)
        print(opcoes)
        indice_resposta = int(input('Escolha uma opção: ')) -1
        resposta = opcoes[indice_resposta]

        print(indice_resposta, resposta)

        if resposta != resposta_correta:
            print('Errou!\n')
            continue
        
        print('Acertou!\n')
        contador_acertos += 1
        continue
    
    print(f'Você acertou {contador_acertos}/{total}')



perguntas_e_respostas(perguntas)