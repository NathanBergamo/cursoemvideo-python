a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b ==c:
     print('ISÓSCELES')
    elif a != b and a != c and b != c:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')