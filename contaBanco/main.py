from package.bancoFunctions import openMenu, cadastrarConta

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
