"""
Utilizando dicionario para fazer um quiz
primeiro passo listando as perguntas e as opcoes de respostas 
"""
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual a melhor Linguagem?',
        'respostas': {'a': 'Java', 'b': 'Python', 'c': 'Angular', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual o Professor mais legal?',
        'respostas': {'a': 'Joao', 'b': 'Pedro', 'c': 'Maria', },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Qual e melhor?',
        'respostas': {'a': 'banana', 'b': 'maca', 'c': 'kiwi', },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Qual e melhor?',
        'respostas': {'a': 'uva', 'b': 'morango', 'c': 'manga', },
        'resposta_certa': 'b',
    },
    'Pergunta 5': {
        'pergunta': 'Qual e melhor artista?',
        'respostas': {'a': 'Mulango', 'b': 'Tiradentes', 'c': 'Tirulipa', },
        'resposta_certa': 'c',
    },
    'Pergunta 6': {
        'pergunta': 'Qual a melhor musica?',
        'respostas': {'a': 'Macarena', 'b': 'menina veneno', 'c': 'vamos fugir', },
        'resposta_certa': 'b',
    },
    'Pergunta 7': {
        'pergunta': 'Qual a melhor comida?',
        'respostas': {'a': 'Macarrão', 'b': 'ovo', 'c': 'figado', },
        'resposta_certa': 'a',
    },
    'Pergunta 8': {
        'pergunta': 'Qual a melhor bebida?',
        'respostas': {'a': 'cha de boldo', 'b': 'Tampico', 'c': 'Caipirinha', },
        'resposta_certa': 'c',
    },
    'Pergunta 9': {
        'pergunta': 'Qual a melhor pao?',
        'respostas': {'a': 'pao de forma', 'b': 'pao de queijo', 'c': 'pao de leite', },
        'resposta_certa': 'a',
    }
    ,
    'Pergunta 10': {
        'pergunta': 'Qual selecione o mais divo?',
        'respostas': {'a': 'Tom holland', 'b': 'Leo dicaprio', 'c': 'Brad pitt', },
        'resposta_certa': 'a',
    }
}
print()
# indice_p indice da pergunta, indice_op indice da opçao
for indice_p, txtpergunta in perguntas.items():
    print(f'{indice_p}: {txtpergunta["pergunta"]}')

    print('respostas: ')
    for indice_r, valor_r in txtpergunta['respostas'].items():
        print(f'[{indice_r}]: {valor_r}')

# verificando as respostas do usuario
    resposta_usuario = input('escolha a opcao ')

    if resposta_usuario == txtpergunta['resposta_certa']:
        print('acertou')
        
    else:
        print('errou')
        print()

    