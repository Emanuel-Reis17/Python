'''
Sets: É uma coleção desordenada de elementos únicos e imutavéis, não permitindo elementos duplicados e sem ordem específica.
'''
list1 = [10, 20, 30, 40, 50, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)
print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference
print(num1 & num2) # And
