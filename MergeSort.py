import random
def merge(left, right):
    '''
    - Merge two array in ascending order
    - Return a unique array
    '''
    # initialize index:

    i = 0
    j = 0
    new_array = []
    while i < len(left)and j <len(right):
        if left[i]<right[j]:
            new_array.append(left[i])
            i+=1
        else:
            new_array.append(right[j])
            j+=1
    while i<len(left):
         new_array.append(left[i])
         i+=1

    while j<len(right):
        new_array.append(right[j])
        j+=1
    return new_array


def merge_sort(array):
    ''' 
    - Takes an array on n elements
    - Sort it in ascending order
    
    '''

    if len(array) ==1:
        return array
    
    else:
        mid = len(array)//2
        left_array = array[mid:]
        right_array = array[:mid]
        result = merge(merge_sort(left_array),merge_sort(right_array))
        return result
        


# ---------------testing-------------------#
numbers =[]
for i in range(1000):
    numbers.append(random.randint(10, 10000000))


print(merge_sort(numbers))

         


        






