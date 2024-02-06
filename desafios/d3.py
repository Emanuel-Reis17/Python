funcionarios = ['Emanuel', 'Melissa', 'Iara', 'Sofia', 'Alice']
turnoDia = ['Melissa', 'Sofia']
turnoNoite = ['Emanuel', 'Iara', 'Alice']
temCarro = ['Emanuel', 'Iara', 'Melissa']

lista1 = set(temCarro).intersection(turnoNoite)
lista2 = set(temCarro).intersection(turnoDia)
lista3 = set(funcionarios).symmetric_difference(temCarro)
print(lista1, lista2, lista3)