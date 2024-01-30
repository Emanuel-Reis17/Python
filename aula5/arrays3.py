produtos = ['arroz', 'feijão', 'laranja', 'banana', 'maça', 'leite']
item1 = produtos[0]
item1, item2, item3, *outros = produtos

produtos.pop()
print(item1, item2, item3, outros)
