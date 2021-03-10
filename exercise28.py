from random import choice
print('Tente adivinhar qual número o computador está pensando!')
num = int(input('Informe um número de 0 a 5: '))
numpc = choice([0, 1, 2, 3, 4, 5])
if num > 5:
    print('Somente números de 0 a 5!')
elif num == numpc:
    print('O computador pensou no número {}, voce acertou!'.format(numpc))
else:
    print('O computador pensou no número {}, voce errou!'.format(numpc))
