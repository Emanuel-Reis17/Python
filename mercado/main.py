from package.mercadoFunctions import openMenu

while True:
    resposta = str(input('Deseja acessar o mercadinho?(S/N): '))
    if resposta.upper() == 'S':
        print('Iniciando Sessão')
        print('---------- BEM-VINDO AO MERCADINHO ----------')
        openMenu()
    else:
        print('Finalizando a aplicação...')
        break
