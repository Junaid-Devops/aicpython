def binary_search(arr,x,low,high):
    while low<=high:
        midele=low+high//2
        if midele==x:
            return midele
        elif midele<x:
            low=midele+1
        else:
            high=midele-1
    return -1         

list1= [3,4,5,6,7,8,9]    
x=4
print(binary_search(list1,x,0,len(list1)-1))