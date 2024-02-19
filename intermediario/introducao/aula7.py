nome = str(input('Digite o seu nome: '))
if nome:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}.')
    print('Seu nome contém espaços.' if ' ' in nome else 'Seu nome não contém espaços.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')
else:
    print('Nada foi digitado.')