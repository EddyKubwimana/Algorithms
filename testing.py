from insertion_sort import insertion_sort
from merge_sort import merge_sort
import time
import random

# Generating random numbers to sort 
numbers = []
for i in range(10000000):
    numbers.append(random.randint(10,10000000))


# time for merge_sort

startM= time.time()
print(merge_sort(numbers))
endM = time.time()



print("######################################################################################################################################")
print("######################################################################################################################################")
print("######################################################################################################################################")


# time for insertion_sort

startI= time.time()
print(sorted(numbers))
endI = time.time()
print("Insertion sort took : ", endI-startI)

print("Merge-sort took : ", endM-startM)



