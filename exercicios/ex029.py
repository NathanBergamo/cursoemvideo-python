from colorama import Style, Fore
velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(Fore.RED + 'MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de', Fore.LIGHTYELLOW_EX +'R$ {:.2f}'.format(multa))
else:
    print(Fore.LIGHTGREEN_EX + 'Você está dentro do limite de velocidade, PARABÉNS!')
print(Fore.LIGHTYELLOW_EX + 'Tenha uma boa viagem!')
