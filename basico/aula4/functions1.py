def soma(a, b):
    return a + b

def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} em estoque')

print(soma(1, 1))
boas_vindas('Emanuel' )