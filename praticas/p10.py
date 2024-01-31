frutas = ['uva', 'maça', 'banana', 'pera', 'abacati']
buscar = str(input('Verificar fruta: '))

resultado = print("Achei") if buscar.lower() in frutas else print("Não achei")
