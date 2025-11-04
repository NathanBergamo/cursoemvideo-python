from colorama import Style, Fore
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
media = round(media,1)
if media >= 7.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está',Fore.LIGHTGREEN_EX + 'APROVADO !')
elif 5.0 <= media <= 6.9:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está em', Fore.LIGHTYELLOW_EX +'RECUPERAÇÃO !')
else:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está', Fore.LIGHTRED_EX +'REPROVADO ! ')
