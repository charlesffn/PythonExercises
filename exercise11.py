print('Calcule a área de uma parede e a quantidade de tinta necessária para pintá-la.')
altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = altura*largura
tinta = area/2
print('Sua parede possui {:.2f}m² de área e são necessários {:.2f} litros de tinta para pintá-la.'.format(area, tinta))
