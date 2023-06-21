import random
import time
def insertion(array,increase = True):
    '''
    Insertion sort
    Return sorted array in ascending order
    '''
    for i in range(1,len(array)): # [1,5,3,7,0.5,10]
        j = i-1   # j = 0, 1,2
        if increase:
            while j>=0 and array[j]>array[j+1]:# True, False,false
                array[j+1],array[j]= array[j], array[j+1] # [1,5,5,7,0.5,10], same
                j -=1 
        else:
            while j>=0 and array[j]<array[j+1]:# True, False,false
                array[j+1],array[j]= array[j], array[j+1] # [1,5,5,7,0.5,10], same
                j -=1 
    return array


def remove_duplicity(array):
    '''
    remove duplicity
    return an array with unique number
    '''
    sorted = insertion(array)
    result = []
    for i in range(1, len(sorted)):
        if sorted[i-1]==sorted[i]:
            pass
        else:
            result.append(sorted[i])

    return result











def insertion_sort(array):
    '''
    perform insertion sort algorithms
    return a sorted array of the n element of the array
    '''

    checker = True
    while checker:

        checker = False

        for i in range (1,len(array)):
            if array[i-1]>array[i]:
                
                checker = True
                array[i-1] = array[i]
    return array

numbers = [100,10, 20, 1, -10, 5,-5,0,6,10, 20]

print(insertion(numbers,increase=False))

print(remove_duplicity(numbers))




            


