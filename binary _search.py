# performing binary search

def binarySearch(array, value):
    '''
    - Takes an array of n-numbers and a value to search for in that array
    - Sort the array if it is not sorted
    - Return a message if the value is not found or not to inform the user
    - Use n log n runtime algorithm
    '''
    
    array.sort()
    mid = (len(array)//2)
    if len(array)==0:
        return "The list is empty, not found"
    
    if array[mid]==value:
        return "Found"
    elif mid ==0 and array[mid] != value:
        return "Not found"
    
    else:

        if value> array[mid]:
            return binarySearch(array[mid:],value)
        else:
            return binarySearch(array[:mid],value)
    

numbers  = [1,0,8,3,100] # [0,1,3,8,100]
nombre = []

print(binarySearch(numbers,9))
print(binarySearch(nombre, 8))