# Solicita informações ao usuário e cria o dicionário 'pessoa'
pessoa = {
    'nome': input('Digite seu nome: '), 
    'idade': int(input('Digite sua idade: ')), 
    'escolaridade': input('Digite sua escolaridade: '), 
    'cargo': input('Digite o seu cargo: ')
}

# Imprime as informações da pessoa de forma organizada
print("\nInformações da Pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
