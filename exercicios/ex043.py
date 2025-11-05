peso = float(input('QUal é seu peso ? (Kg) '))
altura = float(input('Qual é sua altura ? (m) '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25.0:
    print('Você está no seu PESO IDEAL')
elif 25.0 <= imc < 30.0:
    print('Você está SOBRE-PESO')
elif 30.0 <= imc < 40.0:
    print('Você se encontra no estado de OBESIDADE')
else:
    print('Você encontra em OBESIDADE MÓRBIDA, Cuidado !')