import datetime

class Conta:
    dataDeposito = []
    dataSaque = []
    def __init__(self, banco, login, senha, titular, tipoConta): 
        self.banco = banco.upper()
        self.titular = titular.upper()
        self.tipoConta = tipoConta.lower()
        self.saldo = 0
        self.login = login
        self.senha = senha
        self.saquesDiarios = 3
    
    def obterSaldo(self):
        return f'Instituição Financeira: {self.banco} \nTitular: {self.titular} \nSaldo: R${self.saldo} \nData: {self.dataAtual()}\n'

    def depositar(self):
        try:
            deposito = float(input('Quanto deseja depositar?: R$'))
            if deposito > 0:
                porcentagem = lambda x, y: (y/100) * x + x
                self.saldo += porcentagem(deposito, 1.00) if self.tipoConta == 'corrente' else porcentagem(deposito, 0.2)
                self.dataDeposito.append([self.dataAtual(), f'R${deposito}'])
                print('---------- DEPÓSITO REALIZADO ----------')
                print(f'Saldo Atual: R${self.saldo} \nData: {self.dataDeposito[-1]} \n')
            else:
                print('Você não pode adicionar valores menores que R$00.00')
        except ValueError:
            print('Valor inválido!\n')
            self.depositar()
 
    def sacar(self):
        try:
            if self.saquesDiarios > 0:
                saque = float(input('Quanto deseja sacar?: R$'))
                if 50.00 <= saque <= 5000:
                    if saque <= self.saldo:
                        self.saldo -= saque
                        self.saquesDiarios -= 1
                        self.dataSaque.append([self.dataAtual(), f'R${saque}'])
                        print('---------- SAQUE REALIZADO ----------')
                        print(self.obterSaldo())
                    else:
                        print(f'ERROR! Você não pode sacar este valor, você possui apenas R${self.saldo}')
                else:
                    print('ERROR! Você só pode sacar valores entre R$50 à R$5.000')
            else: 
                print('ERROR! Número de saques diários atingido.')
        except ValueError:
            print('Valor inválido')
            self.sacar()
    
    def extrato(self):
        print('----- EXTRATO -----')
        print('Último(s) Depósito(s):')
        for deposito in self.dataDeposito:
            print(deposito)
        print('')
        print('Último(s) Saque(s):')
        for saque in self.dataSaque:
            print(saque)
        print('')
        print(f'Saldo Atual: {self.saldo} \n')
    
    def dataAtual(self):
        data = datetime.datetime.now()
        return f'{data.strftime("%X")} | {data.date()}'
