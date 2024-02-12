shopCars = ('BMW X6', 'BMW i5', 'BMW i8')
userCar = str(input('Digite o nome do carro: '))
if userCar not in shopCars:
    print('Desculpe, este carro não está disponível.')
else:
    print('Este carro está disponível.')