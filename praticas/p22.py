produtos = ['Creme de cabelo', 'Creme de pele', 'Maquiagem', 'Perfume', 'Absorvente']
precos = [10, 25, 20, 49.90, 5]
precos = list(map(lambda x: f'R${str(int(x - (15/100) * x))}', precos))

print(list(zip(produtos, precos)))
