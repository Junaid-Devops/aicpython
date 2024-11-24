def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                # Swap elements
                array[j], array[j + 1] = array[j + 1], array[j]

# Example usage
list1 = [1, 2, -9, -7, 20, 21]
list2=bubblesort(list1)
print(list1)
print(list2)

