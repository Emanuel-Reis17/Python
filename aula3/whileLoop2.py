valor = int(input("Digite o valor do seu produto: "))
while valor > 20:
    valor += valor * 0.10
    print(f"Preço: R${valor}")
    break
