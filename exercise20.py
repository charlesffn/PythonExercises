import random
print('Sorteie uma sequência de alunos.')
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
sequencia = [a1, a2, a3, a4]
random.shuffle(sequencia)
print('A ordem sorteada dos alunos é a seguinte: {}'.format(sequencia))
