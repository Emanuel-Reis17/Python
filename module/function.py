def somar():
    print('Esta função vai somar dois números')

def multi():
    print('Esta função vai multiplicar valores')

def findIndex(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
