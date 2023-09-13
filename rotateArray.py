# Given a an array of lenght N and a K rotator,

def rotateArray(arr, k):

    if k == len(arr):
        return arr
    elif k < len(arr):
        return arr[-k:]+arr[:len(arr)-k]
    else:
        k = k%len(arr)
        return rotateArray(arr,k)



# Testing 

numbers = [1,3,8,9,9]
print(numbers)
print(rotateArray(numbers, 12))