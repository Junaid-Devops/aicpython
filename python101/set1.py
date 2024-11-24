set1={10,12,16,30}
set2={11,12,16,31}

print(set1|set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1&set2)

set3={10,12,16,30}
set4={11,12,16,31}

print(set3-set4)
print (set3.difference(set4))

##symmatic 
set5={10,12,16,30}
set6={11,12,16,31}
print (set6.sysmmetric_difference(set5))
