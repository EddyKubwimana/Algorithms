import random
import time
def insertion(array):
    '''
    Insertion sort
    Return sorted array in ascending order
    '''
    for i in range(1,len(array)): # [1,5,3,7,0.5,10]
        j = i-1   # j = 0, 1,2
        while j>=0 and array[j]>array[j+1]:# True, False,false
            array[j+1],array[j]= array[j], array[j+1] # [1,5,5,7,0.5,10], same
            print(array)
            j -=1 
    return array



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

numbers = [100,10, 20, 1, -10, 5,-5,0,6]

starttime = time.time()
print(starttime)
print(insertion(numbers))
endtime = time.time()
print(endtime-starttime)


starttime2 = time.time()
print(insertion_sort(numbers))
endtime2 = time.time()
print(endtime2-starttime2)


            


