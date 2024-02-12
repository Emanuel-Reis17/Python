paises = [['Brasil', 'Brasíia'], ['Nova Zelândia', 'Auckland'], ['Estados Unidos', 'Washington, D.C'], ['Canadá', 'Ottawa'], ['França', 'Paris'], ['México', 'Cidade do México']]
userCountry = str(input('Digite o nome do país: '))
for p in paises:
    if userCountry == p[0]:
        print(f'A capital de {p[0]} é {p[1]}')
        break
else:
    print('Desculpe, não temos informações sobre a capital desse país')