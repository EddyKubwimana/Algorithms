def insertion_sort(array):
    '''
    function to perform insertion sort algorithms
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


numbers = [20,30, -10, 33, 10]
print(insertion_sort(numbers))
            


