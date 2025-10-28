from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    diferenca = 18 - idade
    alistamento = atual + diferenca
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('Ainda faltam {} anos para o seu alistamento'.format(diferenca))
    print('Seu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    diferenca = idade - 18
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('Você ja deveria ter se alistado há {} anos'.format(diferenca))