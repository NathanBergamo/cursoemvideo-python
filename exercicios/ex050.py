cont = 0
s = 0
for c in range(1, 7):
        n = int(input('Digite o {}º valor: '.format(c)))
        if n % 2 == 0:
            s += n
            cont += 1
print('Voce informou {} número(s) pares e a soma foi: {}'.format(cont,s))


