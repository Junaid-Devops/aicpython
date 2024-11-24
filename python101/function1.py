# def first(a,b,c=15):
#     result=a-b+c
#     return result
    
# somoftwo=first(a=7,b=10,c=8)
# print(somoftwo)

## nested function

# def outerf():
#     a='python'

#     def innerf():
#         print(a)
#     innerf() 
# outerf()

# x=lambda a,b,c:a+b+c
# greet=lambda : print('python')
# greet()
# print(x(7,8,15))

# def max_element(input_list):
#     maxelement=input_list[0]
#     for num in input_list:
#         if num>maxelement:
#             maxelement=num
#     return maxelement
# list1=[10,45,12,32]
# print(max_element(list1))

def factotial(num):
    #base case
    if num==1:
        return 1
    else:
        return num*factotial(num-1) # return 5
print(factotial(5))    

















