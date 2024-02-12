frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []
# for item in frutas1:
#     if 'w' in item:
#         frutas2.append(item)

frutas2 = [item for item in frutas1 if 'n' in item]

print(frutas2)