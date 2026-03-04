print('Formas de impressão ==============')

print('Estou aprendendo python', 'Hoje foi a primeira aula', sep='-') #Concatenação + separador

print('Estou aprendendo python', 'Hoje foi a primeira aula', sep='-', end='***\n') #Finalizador

print('sabado', 'Dia de estudar', sep='-', end='T-T\n')

print('777', '558', '333', sep='.', end='-')
print('20')

print('=================================')

print("texto'texto entre aspas simples'")

print('texto"texto entre aspas duplas"')

print('=================================')

print('Laço de repetição ================')
nomes = ['Lara','Julia','Luiza']
for nome in nomes:
    print(nome)

print('=================================')

print('for/else =========================')
nomes = ['Lara','Julia','Luiza']
for nome in nomes:
    print(nome)
else:
    print("Todos os nome foram listados com sucesso")

print('=================================')

print('Separar a letra, For string ==============')
palavra = "Vamos estudar Python"
for letra in palavra:
    print(letra)

print('=================================')

print('for listando vetor ===============')
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Asa Norte'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])
    # break

print('=================================')

print('For com  break ==============')
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Asa Norte'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break

print('=================================')

print('For com continue ==============')
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Asa Norte'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])

print('=================================')

print('For com range que retorna o valor do contador o conteudo ==============')
for numero in range(10):
    if numero % 2 == 0:
        print("O número", numero, "é par")

print('=================================')

print('For com enumerete ==============')
for i, j in enumerate(range(10, 1, - 1)):
    print(i, j)
    
print('=================================')

print('For alinhado =====================')
for numero_coluna1 in range(2, 5):
    print("Tabuada do ", numero_coluna1)
    for numero_coluna2 in range(11):
        print(numero_coluna1, "x", numero_coluna2, " = ", numero_coluna1 * numero_coluna2)