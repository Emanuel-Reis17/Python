# Testando modules e packages
from module import Cliente
from package.compra import compra

cliente1 = Cliente(1, 'Emanuel Reis', 'PC Gamer', 'Custo benefício')
compra(cliente1.nome, 'PC Gamer', 2399.90)
cliente1.imprimir()

