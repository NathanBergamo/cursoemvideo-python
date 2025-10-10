from colorama import Style, Fore
num = int(input(Fore.LIGHTMAGENTA_EX + 'Me diga um número: '))
rest = num % 2
if rest == 0:
    print(Fore.LIGHTWHITE_EX + 'O número {} é PAR'.format(num))
else:
    print(Fore.LIGHTWHITE_EX + 'o número {} É IMPAR'.format(num))