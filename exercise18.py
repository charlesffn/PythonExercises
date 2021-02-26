import math
print('Calcule o seno, cosseno e tangente.')
x = int(input('Informe um ângulo: '))
a = math.radians(x)
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)
print('Para o ângulo de {:.2f}°, o seno é {:.5f}, o coseno é {:.5f} e a tangente é {:.5f}.'.format(x, sen, cos, tan))
