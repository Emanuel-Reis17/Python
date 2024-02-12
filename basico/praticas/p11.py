nomes1 = ('Emanuel', 'Lucas', 'Melissa', 'Luana', 'Luana', 'Emerson', 'Vitor', 'Ednei')
nomes2 = ('Emanuel', 'Lucas', 'Luana', 'Luana', 'Ednei', 'Giulia')

names1 = set(nomes1)
names2 = set(nomes2)

# print(names1)
print(names1 - names2)
print(names1 | names2)
print(names1 ^ names2)
