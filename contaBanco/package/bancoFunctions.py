def openMenu(conta):
    try:
        print('---------- MENU DE OPÇÕES ----------')
        print('[1] - Depositar \n[2] - Obter Saldo \n[3] - Sacar \n[4] - Exibir Extrato \n[5, ...] - Sair \n')
        resposta = int(input('Digite o número da opção que deseja realizar: '))
        print()
        if resposta == 1:
            conta.depositar()
            openMenu(conta)
        elif resposta == 2:
            print(conta.obterSaldo())
            openMenu(conta)
        elif resposta == 3:
            conta.sacar()
            openMenu(conta)
        elif resposta == 4:
            conta.extrato()
            openMenu(conta)
        else:
            print('Encerrando sessão da conta...')
            return False
    except ValueError:
        print('Valor inválido. Por favor insira o valor corretamente.')
        openMenu(conta)