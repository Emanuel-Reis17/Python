"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
user_num = input("Digite um número inteiro: ")
if user_num.isdigit():
    num = int(user_num)
    print(f'O número {num} é par.' if num % 2 == 0 else f'O número {num} ímpar.')
else:
    print('O valor digitado não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
user_horario = input('Digite as horas: ')
if user_horario.isdigit():
    horario = int(user_horario)
    if 0 <= horario <= 11:
        print(f'Bom dia! São {horario}hs.')
    elif 12 <= horario <= 17:
        print(f'Boa tarde! São {horario}hs.')
    else:
        print(f'Boa noite! São {horario}hs.')
else:
    print('O valor digitado não é um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
username = input('Digite o seu nome: ')
if not username.isdigit():
    if len(username)
else:
    print('O valor digitado não pode ser um número.')