from datetime import datetime
# Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# Criar o objeto
usuario1 = Funcionarios('Emanuel', 'Reis', 2005)
usuario2 = Funcionarios('Melissa', 'Reis', 2008)
usuario3 = Funcionarios('Iara', 'Reis', 2012)

print(Funcionarios.idade_funcionario(usuario1))
