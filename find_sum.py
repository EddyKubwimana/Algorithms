# find if a list contains at least two values that sum up to given y number:
# the algorithm has to be of order O( n log n )
from merge_sort import merge_sort
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
       
       array_prime = difference(array, value)
       array.extend(array_prime)
    
       sorted_array = merge_sort(array)

       for i in range(1,len(sorted_array)):
              if sorted_array[i-1]== sorted_array[i]:
                     return True
       return False


       
    




# -----------------------------Testing------------------------------------------------------------------------#

array = [1,7,9,9,8,9]

print(find_sum(array,8))

