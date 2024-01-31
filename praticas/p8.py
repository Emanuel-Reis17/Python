# Cálculo de porcentagem
def calcPorcentagem(porcentagem, valor):
    return f'O salário final é de: R${str(int(((porcentagem / 100) * valor + valor)))}'

salario = float(input('Digite o salário:'))
porcentagem = float(input('Digite a porcentagem desejada: '))
print(calcPorcentagem(porcentagem, salario))
