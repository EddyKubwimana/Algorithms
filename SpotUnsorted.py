# Writing algorithm that use  divide and conquer method to check whether an array is sorted in ascending order


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

def merge_check(right, left):
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

numbers = []
numbers2 = []
for i in range(9):
    numbers.append(10+i)
    if i ==5:
       numbers2.append(-100)
    else:
        numbers2.append(10+i)


     
print(spotsorted(numbers))
print(spotsorted(numbers2))
print(numbers)
print(numbers2)
