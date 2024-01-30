# Diz em que estado da vida se encontra
idade = int(input("Quantos anos você tem?: "))

if idade < 11:
    print(f"Sua idade é {idade}, você é uma criança.")
elif 11 <= idade <= 18:
    print(f"Sua idade é {idade}, você é um(a) adolescente.")
elif 18 < idade < 25:
    print(f"Sua idade é {idade}, você é um(a) jovem.")
elif idade <= 65:
    print(f"Sua idade é {idade}, você é um(a) adulto(a).")
else:
    print(f"Sua idade é {idade}, você é um(a) idoso(a)")
