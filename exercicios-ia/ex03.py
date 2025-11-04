preco = float(input('Preço da compra: R$ '))
print('--' * 15)
print('*** FORMAS DE PAGAMENTO ***')
print('--' * 15)
print('[ 1 ] á vista no dinheiro/pix') #10% de desconto
print('[ 2 ] á vista no cartão') # 5% de desconto
print('[ 3 ] 2x no cartão') # Preço normal
print('[ 4 ] 3X ou mais no cartão') # 20% de juros
print('--' * 15)
opcao = int(input('Como deseja pagar ? '))
if opcao == 1:
    total = preco - (preco * 10 /100)
    print('Escolhendo a opção 1, o preço fica R${:.2f} '.format(total))
elif opcao == 2:
    total = preco - (preco * 5 /100)
    print('Escolhendo a opção 2, o preço fica R${:.2f}'.format(total))
elif opcao == 3:
    print('Escolhendo a opção 3, não há alteração no valor, o preço fica R${:.2f}'.format(preco))
elif opcao == 4:
    total = preco + (preco * 20/100)
    print('Escolhendo a opção 4, o preço fica R${:.2f}'.format(total))
else:
    print('Opçao INVÁLIDA ! Tente novamente.')