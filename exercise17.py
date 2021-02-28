from math import hypot
print('Calcule a hipotenusa.')
catop = float(input('Informe o comprimento do cateto oposto: '))
catad = float(input('Informe o comprimento do cateto adjacente: '))
hipo = hypot(catop, catad)
print('Para cateto oposto {} e cateto adjacente {}, a hipotenusa é {:.3f}.'.format(catop, catad, hipo))
