# Realizar a compra de um produto com 3 tentativas
print("Celular Samsung Galaxy S24 \nPreço: R$4.500,00")

for valor in range(3):
    valor = int(input("Digite o valor para realizar a compra: "))
    if valor == 4500:
        print("Compra realizada com sucesso!")
        break
    print("O valor digitado não corresponde ao preço do produto.")
else:
    print("Falha ao realizar a compra...")
