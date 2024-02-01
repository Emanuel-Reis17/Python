# Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimetno):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimetno

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

# Criar o objeto
usuario1 = Funcionarios('Emanuel', 'Reis', '00/00/0000')
usuario2 = Funcionarios('Melissa', 'Reis', '99/99/9999')
usuario3 = Funcionarios('Iara', 'Reis', '77/77/7777')

print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
