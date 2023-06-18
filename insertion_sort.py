import random

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
                print( array[i-1], array[i])
                checker = True
                array[i-1], array[i] = array[i], array[i-1]
            else:
        
                break

    
    return array

numbers = [6.441882568521997, 9.129469771028411, 8.085007999916666, 0.6830121262619548, 5.719945981926121, 3.3625403059347168, 0.0619248581640619, 1.2868810913334217, 4.704578031092196, 2.8700843094668347]

print(insertion_sort(numbers))
            


