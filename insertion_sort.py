import random
import time
def insertion(array):
    '''
    Insertion sort
    Return sorted array in ascending order
    '''
    for i in range(1,len(array)): # [1,5,3,7,0.5,10]
        key = array[i] # 5,3,7
        j = i-1   # j = 0, 1,2
        while j>0 and array[j]>key:# True, False,false
            array[j+1]= array[j] # [1,5,5,7,0.5,10], same
            j -=1 # 0
        array[j+1] = key # 3,[1,3,5,7,0.5,10], same
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
                array[i-1], array[i] = array[i], array[i-1]
    return array

numbers = [6.441882568521997, 9.129469771028411, 8.085007999916666, 0.6830121262619548, 5.719945981926121, 3.3625403059347168, 0.0619248581640619, 1.2868810913334217, 4.704578031092196, 2.8700843094668347]
starttime = time.time()
print(starttime)
print(insertion_sort(numbers))
endtime = time.time()
print(endtime-starttime)


starttime2 = time.time()
print(insertion_sort(numbers))
endtime2 = time.time()
print(endtime2-starttime2)


            


