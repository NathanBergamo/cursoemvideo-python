print('------LOJA DO NATHAN------')
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
escolha = int(input('Qual é a opção ? '))
if escolha == 1:
    total = preco - (preco * 10 / 100)
elif escolha == 2:
    total = preco - (preco * 5 / 100)
    print(total)
elif escolha == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif escolha == 4:
    parcelas = int(input('Quantas parcelas ? '))
    total = preco + (preco * 20 / 100)
    valor = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcelas, valor))
else:
    total = preco
    print('Opção inválida, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

