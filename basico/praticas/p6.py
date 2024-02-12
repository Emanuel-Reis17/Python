# Função para cadastrar um produto

def cadastrarProduto(nome='Underfined', preco=0):
    print('-----------------------------')
    print(f'Produto: {str(nome)} \nPreço: R${str(preco)}')

def criarEmpresa():
    nome_empresa = str(input("Digite a Razão Social: "))
    cnpj = str(input("Digite o CNPJ: "))
    servico = str(input("Digite os serviços prestados da empresa: "))
    print('------------------------------------')
    print(f'Razão Social: {nome_empresa} \nCNPJ: {cnpj} \nServiço(s): {servico}')

# cadastrarProduto('Livro', 89)
criarEmpresa()
