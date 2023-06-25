# find if a list contains at least two values that sum up to given y number:
# the algorithm has to be of order O( n log n )

def difference(array, value):
       '''
       - Takes an array
       - Substract from each n-element by given value
       - Return the the difference array
       - Use in-place operation when substracting  
       '''
       for i in range(len(array)):
             array[i] = array[i]-value
       return array

def find_sum(array, value):
    array.sort()
    




# -----------------------------Testing------------------------------------------------------------------------#

array = [1,7,9]
print(difference(array, 5))
