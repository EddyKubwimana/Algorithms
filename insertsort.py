def insertion_sort(array):
    '''
    - Return a sorted array
    - Using O(n^2) time complexity

    '''
    # Outer loop for going through all element
    for i in range(len(array)):
        key = array[i]
        j = i-1
         
        # Inner loop for checking the superiority or inferiority
        while j>=0 and key>array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array



#----------------------------------------------testing----------------------------------------------#
numbers = [1,10,-10,-2,2,8]
print(insertion_sort(numbers))
