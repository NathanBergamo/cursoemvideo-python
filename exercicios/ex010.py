real = float(input('Quanto voce tem na carteira ? R$'))
dolar = real / 5.82
euros = real / 6.07
print('Com o valor de R${:.2f}, você pode comprar: \n ${:.2f} \n €{:.2f}'.format(real, dolar, euros))