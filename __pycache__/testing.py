from merge_sort import merge_sort
from insertion_sort import insertion_sort
import time
import random

# Generating random numbers to sort 
numbers = []
for i in range(1000000):
    numbers.append(random.uniform(0,1000000))


# time for merge_sort

startM= time.time()
print(merge_sort(numbers))
endM = time.time()
print("Merge-sort took : ", endM-startM)


#time for insertion_sort

startI= time.time()
print(insertion_sort(numbers))
endI = time.time()
print("Merge-sort took : ", endI-startI)



