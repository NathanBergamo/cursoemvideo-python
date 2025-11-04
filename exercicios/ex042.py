a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b == c:
        print('Os segmentos acima PODE FORMAR triângulo EQUILÁTERO')
    elif a == b or a == c or b ==c:
     print('Os segmentos acima PODEM FORMAR triângulo ISÓSCELES')
    elif a != b and a != c and b != c:
        print('Os segmentos acima PODEM FORMAR triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')