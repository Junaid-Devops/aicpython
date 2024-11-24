# def search(arr,x):
#     for i in range(len(arr)):
#         if arr[i] ==x:
#             return i
#         return -1

# while low <=high:
#     mid = low+ high //2

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1


list1=[4,10,11,56,7]
print(linear_search(list1,9))
evaluat= linear_search(list1,9)



