frutas = ['Maçã', 'Banana', 'Manga', 'Uva']
vegetais = ['Cenoura', 'Tomate', 'Pimentão', 'Alface']
c = 0
for f in frutas:
    for v in vegetais:
        print(f, v)
        c += 1
print(f'Total de combinações: {c}')