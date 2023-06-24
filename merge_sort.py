# Divide and conquer algorithm
from insertion_sort import insertion_sort
def merge(left,right):
    '''- Merge two arrays together
       - Returns a combined array
    '''
    merged = []
    right_index, left_index = 0, 0
    while left_index<len(left) and right_index < len(right):
        
        if left[left_index] <=right[right_index]:
            merged.append(left[left_index])
            left_index+= 1
        else:
            merged.append(right[right_index])
            right_index+=1

    while left_index <len(left):
         merged.append(left[left_index])
         left_index+= 1
        
    while right_index < len(right):
        merged.append(right[right_index])
        right_index+=1

    return merged

def merge_sort(array):
    '''
    - Takes array of integer
    - Return a sorted array
    - Use nlogn runtime in the worst case scenario
    '''
    if len(array)==1:
        return array
    else:
        mid = len(array)//2
        left = array[:mid]
        right= array[mid:]
        
        left = merge_sort(left)
        right = merge_sort(right)

        merged = merge(left, right)

        return merged

       

#.....................testing the function written above.....................#

numbers= [0,-100,1.7, 80, 467, -1000]
print(merge_sort(numbers))
print(insertion_sort(numbers))






    
    
    

    
    