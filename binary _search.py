# performing binary search

def binarySearch(array, value):
    '''
    - Takes an array of n-numbers and a value to search for in that array
    - Sort the array if it is not sorted
    - Return a message if the value is not found or not to inform the user
    - Use n log n runtime algorithm
    '''
    mid = int((len(array)/2))
    if array[mid] == value:
        return "Found"
    elif mid == 0:
        return "Not found"
       
    else:
        if array[mid]>value:
            binarySearch(array[:mid])
        else:
            binarySearch(array[mid:])

numbers  = [1,3, 60, 65, 8]
print(binarySearch(numbers,60))