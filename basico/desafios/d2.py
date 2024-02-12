rendimento = int(input('Qual é o rendimento da lata?: '))
altura = int(input('Qual é a altura da parede?: '))
largura = int(input('Qual é a largura da parede?: '))

def calcPintura(r, a, l):
    return print(f'Você precisa de {a * l / r} latas de tinta')
calcPintura(rendimento, altura, largura)