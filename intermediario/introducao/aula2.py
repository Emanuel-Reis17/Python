nome = str(input('Digite o seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura**2)

print(f'Sr.{nome=}, seu IMC é de {imc=:.2f}')
