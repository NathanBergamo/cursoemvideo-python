from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade < 10:
    print('Classificação: MIRIM')
elif idade < 15:
    print('Classificação: INFANTIL')
elif idade < 20:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
