def findTarget(nums, target):
    '''
    - Search two numbers that sum up to a target
    - Return the index of those two numbers

    '''

    for i in range(len(nums)):
        key = target-nums[i]
        if key in nums:
             index = nums.index(key)
             if i != index:
                 return [i,index]


    return None

#===============================================================================================================================#

numbers = [1,0,9,8,10,11,13]  

print(findTarget(numbers,20))

