try:
    valor = int(input('Digite o valor do seu produto: '))
    print(type(valor))
except ValueError:
    print('Favor digitar um valor e números')
else:
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)
finally:
    print('Código okay')

print('mais código abaixo')