produtos = []
quantidade = int(input("Quantos produtos quer adicionar?: "))
while len(produtos) != quantidade:
    print(produtos)
    resultado = str(input("Digite o nome do produto: ")).lower()
    if resultado.lower() not in produtos:
        produtos.append(resultado)
    else:
        print("Este produto já existe!")
else:
    print("Quantidade limite atingido!\n----------Produto cadastrados----------")
    for produto in produtos:
        print(produto)