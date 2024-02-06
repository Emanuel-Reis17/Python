from package.conta import Conta
from package.bancoFunctions import openMenu

def cadastrarConta():
    print('---------- INICIANDO CADASTRO ----------')
    banco = str(input('Digite o nome do banco: '))
    titular = str(input('Digite o nome do titular: '))
    tipoConta = str(input('Digite o tipo da conta: '))
    login = str(input('Cadastre um login: '))
    senha = str(input('Cadastre uma senha: '))
    print('---------- CONTA CADASTRADA ----------')
    return Conta(banco, login, senha, titular, tipoConta)

conta1 = cadastrarConta()
while True:
    resposta = str(input('Deseja entrar na conta?(S/N): '))
    if resposta.upper() == 'S':
        login = str(input('Insira o login: '))
        senha = str(input('Insira o senha: '))
        if login == conta1.login and senha == conta1.senha:
            print('Iniciando sessão...')
            openMenu(conta1)
        else:
            print("Erro ao entrar a conta.")
    else:
        print('Finalizando a aplicação...')
        break