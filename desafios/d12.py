idade = int(input('Digite sua idade: '))
if idade < 13:
    print('Você é criança.')
elif 13 <= idade <= 20:
    print('Você é adolescente.')
else:
    print('Você é adulto.')