#calculando o preço de uma passagem cobrando R$ 0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas
from tkinter.ttk import Style

from colorama import Style, Fore
dist = float(input('Qual é a distância da sua viagem: '))
if dist > 200:
    v = dist * 0.45
    print(Fore.LIGHTCYAN_EX + '-=-' * 8)
    print(Fore.LIGHTYELLOW_EX + 'VIAGEM ACIMA DE 200km !'.format(dist))
    print(Fore.LIGHTCYAN_EX + '-=-' * 8)
    print(Fore.RESET + 'Você está prestes a começar uma viagem de', Fore.LIGHTBLUE_EX + '{:.1f}km.'.format(dist))
    print(Fore.RESET + 'O preço da sua passagem será de', Fore.LIGHTBLUE_EX + 'R${:.2f}'.format(v))
else:
    v = dist * 0.50
    print(Fore.LIGHTCYAN_EX + '-=-' * 8)
    print(Fore.LIGHTYELLOW_EX + 'VIAGEM ABAIXO DE 200km !'.format(dist))
    print(Fore.LIGHTCYAN_EX + '-=-' *8)
    print(Fore.RESET + 'Você está prestes a começar uma viagem de', Fore.LIGHTBLUE_EX + '{:.1f}km.'.format(dist))
    print(Fore.RESET + 'O preço da sua passagem será de', Fore.LIGHTBLUE_EX + 'R${:.2f}'.format(v))

    '''v = dist * 0.45 if dist > 200 else dist * 0.50'''



