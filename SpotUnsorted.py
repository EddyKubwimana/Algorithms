# Writing algorithm that use 

def spotsorted(array):
    '''
    - Takes an array
    - Return True if the array is sorted
    - Return False if the array is not sorted
    - Use O (n log n)
    '''
    if len(array)== 1 or len(array)==0:
        return True

    if len(array)==2:
        return merge_check(array)
    else:
        mid= len(array)//2
        left = spotsorted(array[:mid])
        right = spotsorted(array[mid:])
        return merge_check(left) and merge_check(right)

def merge_check(right):
    '''
    - Takes an array and compare two successive number in an array 
    - Return True if they are sorted in ascending order
    - Return False if they are not sorted in ascending order

    '''
    if isinstance(right, bool):
        return right
    elif right[0]>right[1]:
        return False
    else: 
      return True


numbers = [3,10, 11,20,50,10]
print(spotsorted(numbers))
