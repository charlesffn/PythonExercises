name = str(input('Digite seu nome completo: ')).strip()

print(name.upper())
print(name.lower())

# Tambem poderia ser usado
nospace = len(name) - name.count(' ')
# nospace = (name.replace(" ", ""))
print(nospace)

# Tambem poderia ser usado
# print(name.find(' '))
dividido = name.split()
print(len(dividido[0]))
