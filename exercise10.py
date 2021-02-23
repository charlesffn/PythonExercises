real = float(input('Informe o seu saldo em reais: R$'))
cot = float(input('Informe a cotação do dólar em reais: R$'))
dolar = real/cot
print('Na atual cotação, com R${} você pode comprar US${:.2f}.'.format(real, dolar))
