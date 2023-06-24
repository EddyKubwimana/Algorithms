# Divide and conquer algorithm
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

    




        
        

#.....................testing the function written above.....................#

list1= [1,6,9,11]
list2 = [3,4,5,10]

print(merge(list1,list2))






    
    
    

    
    