cidades = ('São Paulo', 'Salvador', 'Curitiba', 'Rio de Janeiro', 'Florianópolis')
userCidade = str(input('Digite o nome de uma cidade: '))

if userCidade not in cidades:
    print('A cidade não está na lista de cidades.')
else:
    print('A cidade está na lista de cidades.')