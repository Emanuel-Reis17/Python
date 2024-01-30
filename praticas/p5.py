# Acrescentar 10% de comissão no preço do produto
valor_produto = int(input("Digite o preço do produto: "))
valor_produto = valor_produto + (10 / 100) * valor_produto
print(f"O preço final: R${valor_produto}")