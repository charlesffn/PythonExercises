print('Aluguel de Carros')
dias = int(input('Informe quantos dias o carro foi utilizado: '))
km = float(input('Informe a quilometragem percorrida pelo carro: '))
custodiarias = dias*60
custokm = km*0.15
valortotal = custodiarias + custokm
print('O custo total do aluguel do carro foi de R${:.2f}'.format(valortotal))
