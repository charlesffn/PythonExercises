frase = 'Charles Felipe de Freitas do Nascimento'
print(frase[8:40:2])
print(frase[:7])
print(len(frase))
print(frase.count('o', 0, 39))
print(frase.find('les'))
print(frase.replace('Charles', 'Carlos'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '  Aprendo Python  '
print(frase2.strip())
print(frase2.rstrip())

print(frase.split())
print('*'.join(frase.split()))

dividido = frase.split()
print(dividido[3][3])