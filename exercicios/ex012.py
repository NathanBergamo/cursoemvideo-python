preco = float(input('Qual o preço do produto ? R$'))
desconto = preco - (preco * 5 / 100)
print('O produto custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))


#preco = float(input('Qual o preço do produto ? R$'))
#desconto = preco * 0.05
#vf = preco - desconto
#print('O produto custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, vf))