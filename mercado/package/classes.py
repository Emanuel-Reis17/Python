import datetime

data = datetime.datetime.now()

def dataAtual():
    data = datetime.datetime.now()
    return f'{data.strftime("%X")} | {data.date()}'

class Cliente:
    clientes = []
    def __init__(self, nome, endereco, telefone, cpf, dataNascimento):
        cliente = {
            'Nome': nome, 
            'Endereço': endereco, 
            'Telefone': telefone, 
            'CPF': cpf, 
            'Data de Nascimento': self.calcIdade(dataNascimento)
        }
        self.clientes.append(cliente)

    def calcIdade(self, x):
        ano = x.split('/')
        ano = int(ano[-1])
        return True if data.year - ano >= 18 else False
    
    def exibirClientes(self):
        print('\n---------- LISTA DE CLIENTES ----------')
        for cliente in self.clientes:
            for x, y in cliente.items():
                print(f'{x}: {y}')
            print('--------------------')
    
    def buscarCliente(self, cpf):
        for cliente in self.clientes:
            if cpf in cliente['CPF']:
                return cliente['Nome']

class Produto:
    produtos = []
    vendas = []
    def __init__(self, nome, valorCompra, validade, quantidade, estoqueMin, estoqueMax):
        try: 
            produto = {
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
        impostos = [3, 5, 0.2]
        valorLucro = valor + porcentagem(valor, 15)
        for imposto in impostos:
            valorLucro += porcentagem(valorLucro, imposto)
        return valorLucro
        
    def imprimirProdutos(self):
        print('\n---------- LISTA DE PRODUTOS ----------')
        for produto in self.produtos:
            for x, y in produto.items():
                print(f'{x}: {y}') if x != 'Valor da Venda' else print(f'{x}: R${y}')
            print('--------------------')
    
    def compra(self, comprador, cesta=[], valorTotal=0):
        nomeProduto = str(input('Buscar produto: '))
        for produto in self.produtos:

            if nomeProduto in produto['Nome']:
                print(produto['Nome'] + ': R$' + str(produto['Valor da Venda']))
                qtd = int(input('Quantos quer levar?: '))

                if 0 < qtd <= produto['Quantidade']:
                    valor = produto['Valor da Venda'] * qtd
                    produto['Quantidade'] -= qtd
                    valorTotal += valor
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
        formasPagamento = {
            1: 'Dinheiro', 
            2: 'Cartão de Crédito', 
            3: 'Cartão de Débito', 
            4: 'PIX'
        }

        venda = {
            'Comprador': comprador, 
            'Produtos': [x[0] for x in cesta], 
            'Valor': f'R${str(valorTotal)}', 
            'Data da Compra': dataAtual()
        }

        print('\n---------- FORMAS DE PAGAMENTO ----------')
        for x, y in formasPagamento.items():
            print(f'[{x}] - {y}')
        resposta = int(input('Selecione a Forma de Pagamento: '))
        self.vendas.append(venda)

        print('\n---------- COMPRA REALIZADA ----------')
        for produto in cesta:
            print(f'Produto: {produto[0]}     | Quantidade: {produto[1]}     | Preço: {produto[2]}')
        print(f'Forma de pagamento selecionado: {formasPagamento.get(resposta)} \nTotal: R${str(valorTotal)} \nMuito Obrigado, volte sempre! \n')

    def relatorioVendas(self):
        print('\n---------- RELATÓRIO DE VENDAS ----------')
        if len(self.vendas) > 0:
            for venda in self.vendas:
                for x, y in venda.items():
                    print(f'{x}: {y}')
                print('--------------------')
        else:
            print('Nenhuma venda foi realizada.')
