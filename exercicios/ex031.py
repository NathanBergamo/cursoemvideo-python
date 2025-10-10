#calculando o preço de uma passagem cobrando R$ 0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

dist = float(input('Qual é a distância da sua viagem: '))
if dist > 200:
    v = dist * 0.45
    print('Você está prestes a começar uma viagem de {:.1f}km.'.format(dist))
    print('O preço da sua passagem será de R${:.2f}'.format(v))
else:
    v = dist * 0.50
    print('Você está prestes a começar uma viagem de {:.1f}km.'.format(dist))
    print('O preço da sua passagem será de R${:.2f}'.format(v))

    '''v = dist * 0.45 if dist > 200 else dist * 0.50'''



