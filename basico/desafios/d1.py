temperatura = int(input('Qual é a temperatura da carne?: '))
if temperatura < 48:
    print('A carne precisa cozinhar por mais alguns minutos.')
elif temperatura in range(48, 53):
    print('A carne está Selada.')
elif temperatura in range(54, 59):
    print('Ao ponto para o mal-passado.')
elif temperatura in range(60, 64):
    print('Ao ponto.')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem-passado')
elif temperatura in range(71, 99):
    print('Bem-passada.')
else:
    print('Tá queimando, nem coma mais')