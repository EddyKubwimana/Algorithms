#Train min cost given a list of station and changing price for one station to another

def minCost(arr,start,end):
    start = start-1
    end = end-start-1
    arr = arr[start:]+arr[:start]
    
    # right -cost
    right_cost = 0

    for i in range(end):
        right_cost += arr[i]
        
    
    return arr, right_cost


    


numbers = [1,6,9,85,0,9]
print(minCost(numbers,2,4))

