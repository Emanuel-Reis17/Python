import datetime

data = datetime.datetime.now()

idCliente = 0
idProduto = 0

def dataAtual():
    data = datetime.datetime.now()
    return f'{data.strftime("%X")} | {data.date()}'

class Cliente:
    clientes = []
    def __init__(self, nome, endereco, telefone, cpf, dataNascimento):
        global idCliente
        idCliente += 1
        cliente = {
            'ID': idCliente, 
            'Nome': nome.upper(), 
            'Idade': self.calcIdade(dataNascimento), 
            'Endereço': endereco, 
            'Telefone': telefone, 
            'CPF': cpf, 
            'Data de Nascimento': dataNascimento, 
            'Status': self.aprovacaoCliente(dataNascimento)
        }
        self.clientes.append(cliente)

    def calcIdade(self, x):
        ano = x.split('/')
        ano = int(ano[-1])
        return data.year - ano
    
    def exibirClientes(self):
        print('\n---------- LISTA DE CLIENTES ----------')
        for cliente in self.clientes:
            for x, y in cliente.items():
                print(f'{x}: {y}')
            print('--------------------')
    
    def buscarCliente(self, cpf):
        for cliente in self.clientes:
            if cpf == cliente['CPF']:
                return cliente['Nome']
    
    def aprovacaoCliente(self, data):
        idade = self.calcIdade(data)
        return 'Aprovado' if idade >= 18 else 'Negado'

class Produto:
    produtos = []
    vendas = []

    def __init__(self, nome, valorCompra, validade, quantidade, estoqueMin, estoqueMax):
        try:
            global idProduto
            idProduto += 1
            produto = {
                'ID': idProduto, 
                'Nome': nome, 
                'Valor da Compra': f'R${float(valorCompra)}',
                'Valor da Venda': self.calcImposto(valorCompra),
                'Validade': validade,
                'Quantidade': quantidade,
                'Estoque Mínimo': estoqueMin,
                'Estoque Máximo': estoqueMax, 
                'Data do Cadastro': dataAtual()
            }
            self.produtos.append(produto)
        except ValueError:
            print('Preencha os valores corretamente')      
        
    def calcImposto(self, valor):
        porcentagem = lambda x, y: (y/100) * x
        acrescimos = [15, 5, 3, 0.2]
        for imposto in acrescimos:
            valor += porcentagem(valor, imposto)
        valorFinal = float('{:.2f}'.format(valor))
        return valorFinal
        
    def imprimirProdutos(self):
        print('\n---------- LISTA DE PRODUTOS ----------')
        for produto in self.produtos:
            for x, y in produto.items():
                print(f'{x}: {y}') if x != 'Valor da Venda' else print(f'{x}: R${y}')
            print('--------------------')
    
    def compra(self, comprador, cesta=[], valorTotal=0):
        nomeProduto = str(input('Buscar produto: '))
        for produto in self.produtos:

            if nomeProduto in produto['Nome'] or int(nomeProduto) == produto['ID']:
                print(produto['Nome'] + ': R$' + str(produto['Valor da Venda']))
                qtd = int(input('Quantos quer levar?: '))

                if 0 < qtd <= produto['Quantidade']:
                    valor = produto['Valor da Venda'] * qtd
                    produto['Quantidade'] -= qtd
                    valorTotal += float('{:.2f}'.format(valor))
                    cesta.append([produto['Nome'], qtd, 'R$' + str(valor)])
                    print('Produto Adicionado na Cesta')
                    print([x for x in cesta])
                    resposta = str(input('Deseja finalizar o pedido?(S/N): '))
                    
                    if resposta.upper() == 'S':
                        produto
                        print('Indo para o checkout...')
                        self.checkout(comprador, cesta, valorTotal)
                        cesta.clear()
                        return True
                    else:
                        self.compra(comprador, cesta, valorTotal)
                else:
                    print('Você não pode levar essa quantidade.')
                    self.compra(comprador, cesta, valorTotal)
                break
        else:
            print('Produto não encontrado.')
            return False
       
    def checkout(self, comprador, cesta, valorTotal):
        troco = 0.0
        formasPagamento = {
            1: 'Dinheiro', 
            2: 'Cartão de Crédito', 
            3: 'Cartão de Débito', 
            4: 'PIX'
        }
        
        print('\n---------- FORMAS DE PAGAMENTO ----------')
        for x, y in formasPagamento.items():
            print(f'[{x}] - {y}')

        resposta = int(input('Selecione a Forma de Pagamento: '))

        if resposta == 1:
            preco = float(input('Digite o valor passado pelo cliente: R$'))

            if preco >= valorTotal:
                troco = float('{:.2f}'.format(preco - valorTotal))
            else:
                print('Valor insuficiente!')
                return False
            
        venda = {
            'Comprador': comprador, 
            'Produtos': [x[0] for x in cesta], 
            'Valor': f'R${str(valorTotal)}',
            'Troco': f'R${str(troco)}', 
            'Data da Compra': dataAtual()
        }      

        self.vendas.append(venda)

        print('\n---------- COMPRA REALIZADA ----------')
        for produto in cesta:
            print(f'Comprador: {comprador} \nProduto: {produto[0]}     | Quantidade: {produto[1]}     | Preço Total: {produto[2]}')
        print(f'Forma de pagamento selecionado: {formasPagamento.get(resposta)} \nTotal: R${str(valorTotal)} Troco: R${str(troco)} \nMuito Obrigado, volte sempre! \n')

    def relatorioVendas(self):
        print('\n---------- RELATÓRIO DE VENDAS ----------')
        if len(self.vendas) > 0:
            for venda in self.vendas:
                for x, y in venda.items():
                    print(f'{x}: {y}')
                print('--------------------')
        else:
            print('Nenhuma venda foi realizada.')
