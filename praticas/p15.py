def calcDesconto():
    preco = float(input('Digite o preço do produto: R$'))
    desconto = int(input('Digite a porcentagem de desconto do produto: '))
    desconto = (desconto / 100) * preco
    preco -= desconto
    print(f"Preço final: R${int(preco)}\nDesconto: R${int(desconto)}")

calcDesconto()