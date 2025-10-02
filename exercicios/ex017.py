from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))



#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = math.hypot(co,ca)
#print('A hipotenusa vai medir {:.2f}'.format(h))



#from math import pow, sqrt
#com1 = float(input('Comprimento do cateto oposto: '))
#com2 = float(input('Comprimento do cateto adjacente: '))
#co = pow(com1, 2)
#ca = pow(com2, 2)
#soma = co + ca
#h = sqrt(soma)
#print('A hipotenusa vai medir: {:.2f}'.format(h))
