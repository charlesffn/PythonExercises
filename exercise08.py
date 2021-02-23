print('Conversor de medidas')
m = float(input('Digite uma medida em metros: '))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000
print('{}m convertidos para quilômetros é igual a {:.4f}km.'.format(m, km))
print('{}m convertidos para hectômetros é igual a {:.3f}hm.'.format(m, hm))
print('{}m convertidos para decametros é igual a {:.2f}dam.'.format(m, dam))
print('{}m convertidos para decimetros é igual a {:.2f}dm.'.format(m, dm))
print('{}m convertidos para centímetros é igual a {:.2f}cm.'.format(m, cm))
print('{}m convertidos para milímetros é igual a {:.2f}mm.'.format(m, mm))
