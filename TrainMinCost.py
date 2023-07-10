#Train min cost given a list of station and changing price for one station to another

def minCost(arr,start,end):
    right_cost = arr[start:]+arr[-end:]
    left_cost = arr[:len(arr)-start]+arr[start:]
    end_right= end-start
    start = 0
    return right_cost, left_cost, end_right


numbers = [1,6,9,85,0,9]
print(minCost(numbers,1,3))

