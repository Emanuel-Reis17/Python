calcSquare = lambda x: x**2
soma = lambda x, y: x + y
expoente = lambda x, y=2: x**y
duplo = lambda x: calcSquare(x*x)
parImpar = lambda x: 'É par!' if x % 2 == 0 else "É Ímpar"
calcSquareList = lambda x: [calcSquare(i) for i in x]

print(calcSquareList([1, 2, 3, 4, 5]))
