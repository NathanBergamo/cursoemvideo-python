n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
media = round(media,1)
if media >= 7.0:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
    print('O aluno está APROVADO !')
elif 5.0 <= media <= 6.9:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
    print('O aluno está em RECUPERAÇÃO !')
else:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
    print('O aluno está REPROVADO ! ')
