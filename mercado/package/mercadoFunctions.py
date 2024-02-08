from package.classes import Cliente, Produto

def openMenu(conta=False, produtos=False):
    try:
        print('---------- MENU DE OPÇÕES ----------')
        print('[1] - Cadastrar Cliente \n[2] - Exibir Clientes \n[3] - Cadastrar Produto \n[4] - Exibir Produtos \n[5] - Comprar Produtos \n[6] - Relatório de Vendas \n[7..] - Sair')
        resposta = int(input('O que deseja fazer?: '))
        if resposta == 1:
            conta = cadastrarCliente()
            openMenu(conta, produtos)
        elif resposta == 2:
            conta.exibirClientes() if conta else print('Não há contas cadastradas.')
            openMenu(conta, produtos)
        elif resposta == 3:
            produtos = cadastrarProduto()
            openMenu(conta, produtos)
        elif resposta == 4:
            produtos.imprimirProdutos() if produtos else print('Não há produtos cadastrados.')
            openMenu(conta, produtos)
        elif resposta == 5:
            if conta and produtos:
                comprador = conta.buscarCliente(str(input('Digite o CPF do comprador: ')))
                Produto.compra(produtos, comprador)
            else:
                print('É necessário possui uma conta e um produto cadastrado.')
            openMenu(conta, produtos)
        elif resposta == 6:
            Produto.relatorioVendas(produtos) if conta and produtos else print(f'É necessário possui uma conta e um produto cadastrado.')
            openMenu(conta, produtos)
        else:
            print('Encerrando Sessão...')
            return False
    except ValueError:
        print('Valor inválido! \n')
        openMenu(conta, produtos)

def cadastrarCliente():
    # global idCliente
    nome = str(input('Digite o nome do cliente: '))
    endereco = str(input('Digite o endereço do cliente: '))
    telefone = int(input('Digite o telefone do cliente: '))
    cpf = int(input('Digite o CPF do cliente (Não use pontos "." e traços "-"): '))
    dataNascimento = str(input('Digite a data de nascimento do cliente: '))
    # idCliente += 1
    print('Cliente Cadastrado')
    return Cliente(nome, endereco, telefone, cpf, dataNascimento)

def cadastrarProduto():
    nome = str(input('Digite o nome do produto: '))
    valorCompra = float(input('Digite o valor de compra: R$'))
    validade = str(input('Digite a data de Validade: '))
    quantidade = int(input('Digite a quantidade: '))
    estoqueMin = input('Digite o estoque mínimo: ')
    estoqueMax = input('Digite o estoque máximo: ')
    print('Produto Cadastrado')
    return Produto(nome, valorCompra, validade, quantidade, estoqueMin, estoqueMax)
