# Cáculo de aumento de salário usando lambda function
def calcAumento(salario, porcetagem):
    porc = lambda x: (x / 100) * salario
    return f'R${str(salario + porc(porcetagem))}'

print(calcAumento(1320, 30))
