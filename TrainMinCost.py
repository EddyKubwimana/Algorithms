#Train min cost given a list of station and changing price for one station to another

def minCost(arr,start,end):
    ''' 
    - Find the least cost of travelling from one point to another
    '''
    start = start-1
    end = end-start-1
    arr = arr[start:]+arr[:start]
    
    # right -cost
    right_cost = 0

    for i in range(end):
        right_cost += arr[i]


    # left_cost:
    left_cost = arr[0]
    end = end
    for i in range(len(arr)-1,end, -1 ):
        left_cost += arr[i]
        print(arr[i])
        
    
    return arr, right_cost, left_cost


    


numbers = [1,6,9,85,0,9]
print(numbers)
print(minCost(numbers,1,2))

