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

list1=[1,2,3,3,4,4]
list2=[4,4,3,5,6]

merged_list=set(list1) | set(list2)
print(merged_list)

##symmetric
set5={10,12,16,30}
set6={11,12,16,31}
print (set6.symmetric_difference(set5))

## decorator 

def dec1(func):
    def inner():
        print("decorator")
        func()
    return inner
@dec1
def normalfunc():
    print('normal function')
dec_func=dec1(normalfunc)
dec_func()
normalfunc()   

#####

## args
def namelist(*names): ## args
    for name in names:
        print(f"hello,{name}")
    
namelist("sanam","abc","xyz")

## kwargs

def namelist(**names):
    print(names.items()) ## kargs
    for key,value in names.items():
        print(f"{key}:{value}")
    
namelist(name="sanam",age=35, city='dhaka')

####
def add(a,b,c):
    return a+b+c
list1=[10,15,18]
result=add(*list1) ## unpacking a list
print(result)

def dec1(func):
    def inner(a,b):
        print("the division is",a, 'and' , b)
        if b==0:
            print("cant divide")
        return func(a,b)
    return inner
@dec1
def normalfunc(a,b):
    print(a/b)

normalfunc(2,5) 
        