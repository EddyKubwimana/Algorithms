# implementing bubble sort
# import a random module to generating random to test my algorithm

import random

def bubbleSort(array):
    '''
    - Takes an array
    - Return a sorted array
    - Use O(n^2) runtime
    '''
    for i in range(len(array)):
        for j in range(1,len(array)):
            if array[j-1]> array[j]:
                array[j-1],array[j] = array[j], array[j-1]
    return array


#................................................bubble sort........................................................................#

array=[]
for i in range(1000000):
    # generating random number using loop
    array.append(100+i)



print(array)


print()
print("####################################################################################################################################cl")


print(bubbleSort(array))