set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}


# set4 = set1.union(set2)
set4 = set1.symmetric_difference(set3)
# set4 = set2.clear()

print(set4)
