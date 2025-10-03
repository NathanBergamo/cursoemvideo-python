nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'. format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))





'''nomecompl = input('Digite seu nome completo: ')
maisc = nomecompl.upper()
minus = nomecompl.lower()
carac= nomecompl.replace(' ', "")
pnome = nomecompl.split()[0]
letras = len(pnome)
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(maisc))
print('Seu nome em minúsculas é {}'.format(minus))
print('Seu nome tem ao todo {} letras' .format(len(carac)))
print('Seu primeiro nome é {} e ele tem {} letras ' .format(pnome, letras))'''
