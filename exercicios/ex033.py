a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando número menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando número maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O Menor número digitado foi {}'.format(menor))
print('O Maior número digitado foi {}'.format(maior))




'''pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
tv = int(input('Terceiro valor: '))
maior = max(pv, sv, tv)
menor = min(pv, sv, tv)
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))'''
