class Cliente:
    def __init__(self, id, nome, compra, avaliacao):
        self.id = int(id)
        self.nome = nome
        self.compra = compra
        self.avaliacao = avaliacao

    def imprimir(self):
        print('---------- DADOS DO CLIENTE ----------')
        print(f'ID: {str(self.id)} \nNome: {self.nome} \nCompra: {self.compra} \nAvaliação: {self.avaliacao}')
