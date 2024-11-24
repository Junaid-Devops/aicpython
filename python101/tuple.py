numbers=(200,2,5,7,9,10,10,11,300,11,11,11,12,13,13,4,40,40,33,56,22)
frq_dict={}
for num in numbers:
    if num in frq_dict:
        frq_dict[num]+=1
    else:
        frq_dict[num]=1
print(frq_dict)            