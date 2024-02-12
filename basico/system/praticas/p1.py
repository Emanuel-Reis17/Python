import numpy as np

# Semelhante a range()
# print(np.arange(0, 10, 2))

# Retorna um array de zeros
# print(np.zeros((4, 4)))

# Retorna um array de uns
# print(np.ones((5, 5)))

# Retorna um array 2D de uns na diagonal e zeros ao redor
# print(np.eye(5, 5))

# Retorna números espaçados através de um intervalo específico
# print(np.linspace(0, 100, 5))

# Retorna números aleatórios em um dado formato
# print(np.random.rand(5, 5))

# Retorna números aleatórios em um dado formato padrão 
# print(np.random.randn(5))

# Retorna valores aleatórios inteiros
# print(np.random.randint(0, 100, 5))

#
arr = np.random.rand(25)
arr.reshape()
print(arr)