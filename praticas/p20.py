# Contagem de palavras
def contagemPalavras(frase):
    palavras = frase.lower().split()
    contagem_palavras = {}
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    return contagem_palavras

# Contagem de letras
def contar_letras(palavra):
    contagem_letras = {}
    for letra in palavra.lower():
        contagem_letras[letra] = contagem_letras.get(letra, 0) + 1
    return contagem_letras

print(contar_letras('Emanuel'))
print(contagemPalavras('Eu sou Emanuel e sou programador trainee'))
