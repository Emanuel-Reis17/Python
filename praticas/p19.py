# Treinando sets
def checkDifference(list):
    conjunto = set(list)
    return  'Há itens iguais.' if len(conjunto) != len(list) else 'Não há itens iguais'

print(checkDifference([1, 2, 3, 4, 5, 6, 7,5, 4, 23, 56, 66, 23]))
print(checkDifference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
