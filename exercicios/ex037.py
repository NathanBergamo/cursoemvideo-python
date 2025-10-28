n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    b = bin(n)[2:]
    print('{} convertido para BINÁRIO é igual a {}'.format(n, b))
elif escolha == 2:
    o = oct(n)[2:]
    print('{} convertido para OCTAL é igual a {}'. format(n, o))
elif escolha == 3:
    h = hex(n)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}'. format(n, h))
else:
    print('Opção inválida ! Tente novamente...')