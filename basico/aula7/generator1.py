from sys import getsizeof
numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
print(getsizeof(numeros))

numeros = (x * 10 for x in range(1000000))
print(type(numeros))
print(getsizeof(numeros))
