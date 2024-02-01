# Treinand o xargs
def soma(*args):
    total = 0
    for num in args:
        total += num
    print('Total: ' + str(total))

soma(1, 2, 3, 4, 5)

def imprimirDados(**args):
    print('---------------- IMPRIMINDO DADOS ----------------')
    for key, value in args.items():
        print(f'{key}: {str(value)}')
    print('--------------------------------------------------')
imprimirDados(nome='Emanuel', idade=18, cargo='Programador')
