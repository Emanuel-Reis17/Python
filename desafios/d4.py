altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura/100) **2

if imc < 16.9:
    print('Muito abaixo do peso.')
elif 17 <= imc <= 18.4:
    print('Abaixo do peso.')
elif 18.4 <= imc <= 24.9:
    print('Peso normal')
elif 25 <= imc <= 29.9:
    print('Acima do peso')
elif 30 <= imc <= 34.9:
    print('Obesidade grau 1')
elif 34.9 <= imc <= 40:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')