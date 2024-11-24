numbers=[200,2,5,7,9,10,10,11,300,11,11,12,13,13,4,40,33,56,22]
#unique_num=[]
max_element=numbers[0]

for n in numbers:
    if n>max_element:
        max_element=n
print(max_element)