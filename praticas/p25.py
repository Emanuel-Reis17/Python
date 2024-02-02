# Criando classe
class Pessoa:
    def __init__(self, nome, idade, escolaridade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.escolaridade = escolaridade
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        return f'Olá! eu me chamo {self.nome}, tenho {self.idade} anos de idade e trabalho como {self.cargo}.'
    
# Criando instâncias
emanuel = Pessoa('Emanuel Reis', 19, 'Ensino Superior Completo', 'Programador Python Sênior', 25000)
iara = Pessoa('Iara Reis', 17, 'Ensino Médio Completo', 'Designer', 4500)
melissa = Pessoa('Melissa Reis', 18, 'Ensino Superior Incompleto', 'Estágiara Auxiliar Administrativo', 750)

print(emanuel.apresentar())
print(Pessoa.apresentar(iara))
print(Pessoa.apresentar(melissa))

class Produto:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def imprimir(self):
        print('----- DESCRIÇÃO DO PRODUTO -----')
        print(f'Produto: {self.nome} \nCategoria: {self.categoria} \nPreço: R${str(self.preco)}')

produto1 = Produto('Smartphone', 'Dispositivos Móveis', 1599.90)
produto1.imprimir()
