from colorama import Fore, Style
from time import sleep
from random import randint
print(Fore.LIGHTGREEN_EX +'-=-' * 18)
print(Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(Fore.LIGHTGREEN_EX + '-=-' * 18)
num = randint(0,5)
escolha = int(input(Style.RESET_ALL +'Em que número eu pensei? '))
print(Fore.MAGENTA + 'PROCESSANDO...')
sleep(3)
if escolha == num:
    print(Fore.LIGHTYELLOW_EX + 'PARABÉNS! Você conseguiu me vencer! Eu escolhi exatamente o número {}'.format(num))
else:
    print(Fore.RED + 'GANHEI! Eu pensei no número {} e não no {}'.format(num, escolha))
