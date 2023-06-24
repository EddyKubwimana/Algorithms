
def insertion_sort(array,ascending = True):
    '''
    -Takes keys values in an array
    - Returns a sorted array
    - By default, ascending order
    - Set ascending to False for descending order

    '''
    if ascending :
        for i in range(1,len(array),):
            j = i-1
            
            while j>=0 and array[j]> array[j+1]:
                    # in -place sorting by swiping the values in case the above condition is True
                    array[j], array[j+1] = array[j+1], array[j]
                    j -= 1 # decrement j  go back in already sorted array to ensure that they are well sorted before proceeding
        return array
    else:
         
         for i in range(1,len(array),):
            j = i-1
            
            while j>=0 and array[j]< array[j+1]:
                    # in -place sorting by swiping the values in case the above condition is True
                    array[j], array[j+1] = array[j+1], array[j]
                    j -= 1 # decrement j  go back in already sorted array to ensure that they are well sorted before proceeding
            

         return array
    
# ..................Testing...........................................................................................................#




            


